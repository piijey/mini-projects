#!/usr/bin/env python3
"""
Extract table from HTML and save to JSONL format
"""

import json
import re
from html.parser import HTMLParser


class TableExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_tr = False
        self.in_th = False
        self.in_td = False
        self.current_row = []
        self.current_cell = []
        self.rows = []
        self.headers = []

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif tag == "tr" and self.in_table:
            self.in_tr = True
            self.current_row = []
        elif tag == "th" and self.in_tr:
            self.in_th = True
            self.current_cell = []
        elif tag == "td" and self.in_tr:
            self.in_td = True
            self.current_cell = []

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
        elif tag == "tr" and self.in_tr:
            self.in_tr = False
            if self.current_row:
                self.rows.append(self.current_row)
        elif tag == "th" and self.in_th:
            self.in_th = False
            cell_text = " ".join(self.current_cell).strip()
            self.current_row.append(cell_text)
        elif tag == "td" and self.in_td:
            self.in_td = False
            cell_text = " ".join(self.current_cell).strip()
            self.current_row.append(cell_text)

    def handle_data(self, data):
        if self.in_th or self.in_td:
            text = data.strip()
            if text:
                self.current_cell.append(text)


class DetailedTableExtractor(HTMLParser):
    """Extract table with detailed cell content (preserving HTML structure)"""
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_tr = False
        self.in_th = False
        self.in_td = False
        self.current_row = []
        self.current_cell_html = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif tag == "tr" and self.in_table:
            self.in_tr = True
            self.current_row = []
        elif tag == "th" and self.in_tr:
            self.in_th = True
            self.current_cell_html = []
        elif tag == "td" and self.in_tr:
            self.in_td = True
            self.current_cell_html = []
        elif tag == "br" and (self.in_th or self.in_td):
            self.current_cell_html.append("<br />")
        elif tag == "b" and (self.in_th or self.in_td):
            self.current_cell_html.append("<b>")

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
        elif tag == "tr" and self.in_tr:
            self.in_tr = False
            if self.current_row:
                self.rows.append(self.current_row)
        elif tag == "th" and self.in_th:
            self.in_th = False
            cell_html = "".join(self.current_cell_html).strip()
            self.current_row.append(cell_html)
        elif tag == "td" and self.in_td:
            self.in_td = False
            cell_html = "".join(self.current_cell_html).strip()
            self.current_row.append(cell_html)
        elif tag == "b" and (self.in_th or self.in_td):
            self.current_cell_html.append("</b>")

    def handle_data(self, data):
        if self.in_th or self.in_td:
            text = data.strip()
            if text:
                self.current_cell_html.append(text)


def extract_and_clean_text(html_content):
    """
    Extract text from HTML content
    """
    # Remove HTML tags but keep line breaks
    text = re.sub(r"<[^>]+>", " ", html_content)
    # Clean up extra whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_ku_details(html_content):
    """
    Extract detailed information from 句 (poem line) HTML
    
    Expected format:
    上句<br />下句<br />（<b>決まり字</b>上句読み<br />下句読み）

    Example:
    秋の田の かりほの庵の とまをあらみ<br />わが衣手は 露にぬれつつ<br />（<b>あきの</b>たの かりほのいほの とまをあらみ<br />わがころもでは つゆにぬれつつ）
        
    Returns:
    {
        "上句": "上句",
        "下句": "下句",
        "上句読み": "上句読み",
        "下句読み": "下句読み",
        "決まり字": "決まり字"
    }
    """
    result = {}
    
    # Split by parenthesis
    match = re.match(r"^(.*?)（(.*)）$", html_content, re.DOTALL)
    if not match:
        # No parenthesis, just return the poem lines
        parts = re.split(r'<br\s*/?>', html_content)
        if len(parts) >= 1:
            result["上句"] = extract_and_clean_text(parts[0])
        if len(parts) >= 2:
            result["下句"] = extract_and_clean_text(parts[1])
        return result
    
    poem_part = match.group(1)
    reading_part = match.group(2)
    
    # Parse main poem (上句 and 下句)
    poem_lines = re.split(r'<br\s*/?>', poem_part)
    if len(poem_lines) >= 1:
        result["上句"] = extract_and_clean_text(poem_lines[0])
    if len(poem_lines) >= 2:
        result["下句"] = extract_and_clean_text(poem_lines[1])
    
    # Extract 決まり字 from <b> tags
    bold_matches = re.findall(r"<b>(.*?)</b>", reading_part)
    if bold_matches:
        result["決まり字"] = extract_and_clean_text(bold_matches[0])
    
    # Extract readings (remove <b> tags and split by <br />)
    readings_html = re.sub(r"<b>(.*?)</b>", r"\1", reading_part)
    readings = re.split(r'<br\s*/?>', readings_html)
    
    if len(readings) >= 1:
        result["上句読み"] = extract_and_clean_text(readings[0])
    if len(readings) >= 2:
        result["下句読み"] = extract_and_clean_text(readings[1])

    return result


def main():
    html_file = "./data/wikisource_小倉百人一首.html"
    output_file = "./data/wikisource_小倉百人一首_extracted.jsonl"

    # Read HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Extract table with detailed HTML content
    detailed_parser = DetailedTableExtractor()
    detailed_parser.feed(html_content)

    # The first row should be headers
    if detailed_parser.rows:
        headers = detailed_parser.rows[0]
        data_rows = detailed_parser.rows[1:]

        # Write to JSONL
        with open(output_file, "w", encoding="utf-8") as f:
            for row in data_rows:
                # Create dict from headers and row data
                if len(row) >= len(headers):
                    record = {}
                    for i, header in enumerate(headers):
                        header_clean = extract_and_clean_text(header)
                        
                        # Special handling for 句 column
                        if "句" in header_clean:
                            ku_details = extract_ku_details(row[i])
                            record.update(ku_details)
                        else:
                            value_clean = extract_and_clean_text(row[i]) if i < len(row) else ""
                            record[header_clean] = value_clean
                    
                    # Write as JSON line
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")
        
        print(f"✓ Extracted {len(data_rows)} records")
        print(f"✓ Saved to {output_file}")


if __name__ == "__main__":
    main()
