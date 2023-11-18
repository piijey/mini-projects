from torchvision import models
# 実行環境: torchvision 0.16.0

pretrained = models.resnet50(pretrained=True)
print("ResNet50:", pretrained.fc.in_features)
# ResNet50: 2048

# ただし、上記を実行すると、torchvision 0.13 以降では warning が出るので、
# torchvision のバージョンによっては、下記のように weights= ... で指定したほうが良いです
# ... python3.10/site-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.
#  warnings.warn( ... python3.10/site-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=ResNet50_Weights.IMAGENET1K_V1`. You can also use `weights=ResNet50_Weights.DEFAULT` to get the most up-to-date weights.
#  warnings.warn(msg)

pretrained = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
print("ResNet50_Weights.IMAGENET1K_V1:", pretrained.fc.in_features)
# ResNet50_Weights.IMAGENET1K_V1: 2048
# ここで読み込まれる weights のデータは、上記 pretrained=True と同じものです

pretrained = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
print("ResNet50_Weights.IMAGENET1K_V2:", pretrained.fc.in_features)
# ResNet50_Weights.IMAGENET1K_V2: 2048
# こっちを実行すると、新たなデータのダウンロードが行われます
