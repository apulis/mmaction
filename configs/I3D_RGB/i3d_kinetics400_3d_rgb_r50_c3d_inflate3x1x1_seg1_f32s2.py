# model settings
model = dict(
    type='TSN3D',
    backbone=dict(
        type='ResNet_I3D',
        pretrained='torchvision://resnet50',
        depth=50,
        num_stages=4,
        out_indices=[3],
        frozen_stages=-1,
        inflate_freq=((1,1,1), (1,0,1,0), (1,0,1,0,1,0), (0,1,0)),
        inflate_style='3x1x1',
        conv1_kernel_t=5,
        conv1_stride_t=2,
        pool1_kernel_t=1,
        pool1_stride_t=2,
        bn_eval=False,
        partial_bn=False,
        style='pytorch'),
    spatial_temporal_module=dict(
        type='SimpleSpatialTemporalModule',
        spatial_type='avg',
        temporal_size=4,
        spatial_size=7),
    segmental_consensus=dict(
        type='SimpleConsensus',
        consensus_type='avg'),
    cls_head=dict(
        type='ClsHead',
        with_avg_pool=False,
        temporal_feature_size=1,
        spatial_feature_size=1,
        dropout_ratio=0.5,
        in_channels=2048,
        num_classes=400))
train_cfg = None
test_cfg = None
# dataset settings
dataset_type = 'RawFramesDataset'
data_root = 'data/kinetics400/rawframes_train/'
data_root_val = 'data/kinetics400/rawframes_val/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
data = dict(
    videos_per_gpu=8,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file='data/kinetics400/kinetics400_train_list_rawframes.txt',
        img_prefix=data_root,
        img_norm_cfg=img_norm_cfg,
        input_format="NCTHW",
        num_segments=1,
        new_length=32,
        new_step=2,
        random_shift=True,
        modality='RGB',
        image_tmpl='img_{:05d}.jpg',
        img_scale=256,
        input_size=224,
        div_255=False,
        flip_ratio=0.5,
        resize_keep_ratio=True,
        oversample=None,
        random_crop=False,
        more_fix_crop=False,
        multiscale_crop=True,
        scales=[1, 0.8],
        max_distort=0,
        test_mode=False),
    val=dict(
        type=dataset_type,
        ann_file='data/kinetics400/kinetics400_val_list_rawframes.txt',
        img_prefix=data_root_val,
        img_norm_cfg=img_norm_cfg,
        input_format="NCTHW",
        num_segments=1,
        new_length=32,
        new_step=2,
        random_shift=True,
        modality='RGB',
        image_tmpl='img_{:05d}.jpg',
        img_scale=256,
        input_size=224,
        div_255=False,
        flip_ratio=0,
        resize_keep_ratio=True,
        oversample=None,
        random_crop=False,
        more_fix_crop=False,
        multiscale_crop=False,
        test_mode=False),
    test=dict(
        type=dataset_type,
        ann_file='data/kinetics400/kinetics400_val_list_rawframes.txt',
        img_prefix=data_root_val,
        img_norm_cfg=img_norm_cfg,
        input_format="NCTHW",
        num_segments=10,
        new_length=32,
        new_step=2,
        random_shift=True,
        modality='RGB',
        image_tmpl='img_{:05d}.jpg',
        img_scale=256,
        input_size=256,
        div_255=False,
        flip_ratio=0,
        resize_keep_ratio=True,
        oversample='three_crop',
        random_crop=False,
        more_fix_crop=False,
        multiscale_crop=False,
        test_mode=True))
# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=dict(max_norm=40, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    step=[40, 80])
checkpoint_config = dict(interval=1)
# workflow = [('train', 5), ('val', 1)]
workflow = [('train', 1)]
# yapf:disable
log_config = dict(
    interval=20,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
# runtime settings
total_epochs = 100
dist_params = dict(backend='nccl')
log_level = 'INFO'
work_dir = './work_dirs/kinetics400/i3d_kinetics_3d_rgb_r50_c3d_inflate3x1x1_seg1_f32s2_b8_g8_imagenet'
load_from = None
resume_from = None



