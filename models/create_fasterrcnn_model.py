from models import *

def return_fasterrcnn_resnet50_fpn(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_resnet50_fpn.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_mobilenetv3_large_fpn(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_mobilenetv3_large_fpn.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_mobilenetv3_large_320_fpn(
    num_classes, pretrained=True, coco_model=False
):    
    model = fasterrcnn_mobilenetv3_large_320_fpn.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_resnet18(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_resnet18.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_custom_resnet(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_custom_resnet.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_darknet(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_darknet.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_squeezenet1_0(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_squeezenet1_0.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_squeezenet1_1(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_squeezenet1_1.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_mini_darknet(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_mini_darknet.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_squeezenet1_1_small_head(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_squeezenet1_1_small_head.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_mini_squeezenet1_1_small_head(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_mini_squeezenet1_1_small_head.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_mini_squeezenet1_1_tiny_head(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_mini_squeezenet1_1_tiny_head.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_mbv3_small_nano_head(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_mbv3_small_nano_head.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_mini_darknet_nano_head(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_mini_darknet_nano_head.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_efficientnet_b0(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_efficientnet_b0.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_nano(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_nano.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_resnet152(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_resnet152.create_model(
        num_classes, pretrained, coco_model
    )
    return model

def return_fasterrcnn_resnet50_fpn_v2(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_resnet50_fpn_v2.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_convnext_small(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_convnext_small.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_convnext_tiny(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_convnext_tiny.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_vit_b_16(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_vit_b_16.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

def return_fasterrcnn_vit_ti_b_16(
    num_classes, pretrained=True, coco_model=False
):
    model = fasterrcnn_vit_ti_b_16.create_model(
        num_classes, pretrained=pretrained, coco_model=coco_model
    )
    return model

create_model = {
    'fasterrcnn_resnet50_fpn': return_fasterrcnn_resnet50_fpn,
    'fasterrcnn_mobilenetv3_large_fpn': return_fasterrcnn_mobilenetv3_large_fpn,
    'fasterrcnn_mobilenetv3_large_320_fpn': return_fasterrcnn_mobilenetv3_large_320_fpn,
    'fasterrcnn_resnet18': return_fasterrcnn_resnet18,
    'fasterrcnn_custom_resnet': return_fasterrcnn_custom_resnet,
    'fasterrcnn_darknet': return_fasterrcnn_darknet,
    'fasterrcnn_squeezenet1_0': return_fasterrcnn_squeezenet1_0,
    'fasterrcnn_squeezenet1_1': return_fasterrcnn_squeezenet1_1,
    'fasterrcnn_mini_darknet': return_fasterrcnn_mini_darknet,
    'fasterrcnn_squeezenet1_1_small_head': return_fasterrcnn_squeezenet1_1_small_head,
    'fasterrcnn_mini_squeezenet1_1_small_head': return_fasterrcnn_mini_squeezenet1_1_small_head,
    'fasterrcnn_mini_squeezenet1_1_tiny_head': return_fasterrcnn_mini_squeezenet1_1_tiny_head,
    'fasterrcnn_mbv3_small_nano_head': return_fasterrcnn_mbv3_small_nano_head,
    'fasterrcnn_mini_darknet_nano_head': return_fasterrcnn_mini_darknet_nano_head,
    'fasterrcnn_efficientnet_b0': return_fasterrcnn_efficientnet_b0,
    'fasterrcnn_nano': return_fasterrcnn_nano,
    'fasterrcnn_resnet152': return_fasterrcnn_resnet152,
    'fasterrcnn_resnet50_fpn_v2': return_fasterrcnn_resnet50_fpn_v2,
    'fasterrcnn_convnext_small': return_fasterrcnn_convnext_small, 
    'fasterrcnn_convnext_tiny': return_fasterrcnn_convnext_tiny,
    'fasterrcnn_vit_b_16': return_fasterrcnn_vit_b_16,
    'fasterrcnn_vit_ti_b_16': return_fasterrcnn_vit_ti_b_16
}