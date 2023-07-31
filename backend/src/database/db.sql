CREATE DATABASE db_OpenCvRoboXYZDell DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `parametersAdjustFilterImg`(
    id                                          INT NOT NULL AUTO_INCREMENT,
    name                                        CHAR(50),

    FilterColor_Red_Min                         INT,
    FilterColor_Red_Max                         INT,
    FilterColor_Green_Min                       INT,
    FilterColor_Green_Max                       INT,
    FilterColor_Blue_Min                        INT,
    FilterColor_Blue_Max                        INT,

    DefinedAreaForFilter_init_X                 INT,
    DefinedAreaForFilter_init_Y                 INT,

    FilterInterations_Erode                     INT,
    FilterInterations_Dilate                    INT,

    SpliceLineJumpWhiteVer_JumpSize_Min         INT,
    SpliceLineJumpWhiteVer_JumpSize_Max         INT,

    SpliceLineJumpWhiteVer_JumpSize_Field_X     INT,
    SpliceLineJumpWhiteVer_JumpSize_Field_Y     INT,

    SpliceLineJumpWhiteHor_JumpSize_Min         INT,
    SpliceLineJumpWhiteHor_JumpSize_Max         INT,

    SpliceLineJumpWhiteHor_JumpSize_Field_X     INT,
    SpliceLineJumpWhiteHor_JumpSize_Field_Y     INT,

    SpliceLineJumpBlackVer_JumpSize_Min         INT,
    SpliceLineJumpBlackVer_JumpSize_Max         INT,

    SpliceLineJumpBlackVer_JumpSize_Field_X     INT,
    SpliceLineJumpBlackVer_JumpSize_Field_Y     INT,

    SpliceLineJumpBlackHor_JumpSize_Min         INT,
    SpliceLineJumpBlackHor_JumpSize_Max         INT,

    SpliceLineJumpBlackHor_JumpSize_Field_X     INT,
    SpliceLineJumpBlackHor_JumpSize_Field_Y     INT,

    FoundObjectSizeFilter_Min                   INT,
    FoundObjectSizeFilter_Max                   INT,

    VerticalLineSizeFilterOfFoundObject_Min     INT,
    VerticalLineSizeFilterOfFoundObject_Max     INT,

    HorizontalLineSizeFilterOfFoundObject_Min   INT,
    HorizontalLineSizeFilterOfFoundObject_Max   INT,

    parameter01                                 INT,
    parameter02                                 INT,
    parameter03                                 INT,
    parameter04                                 INT,
    parameter05                                 INT,
    parameter06                                 INT,
    parameter07                                 INT,
    parameter08                                 INT,
    parameter09                                 INT,
    parameter10                                 INT,

    ConstResolutionPixelMm_X                    DECIMAL(15,6),
    ConstResolutionPixelMm_Y                    DECIMAL(15,6),

    parameterReal01                             DECIMAL(15,6),
    parameterReal02                             DECIMAL(15,6),
    parameterReal03                             DECIMAL(15,6),
    parameterReal04                             DECIMAL(15,6),
    parameterReal05                             DECIMAL(15,6),
    parameterReal06                             DECIMAL(15,6),
    parameterReal07                             DECIMAL(15,6),
    parameterReal08                             DECIMAL(15,6),

    PRIMARY KEY(id)
);

INSERT INTO `parametersAdjustFilterImg`
VALUES (
        'Init',0,0,0,0,0,
        0,0, 
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,
        0,0,0,0,0,0,0,0,      
        0,0,
        0.0,0.0,
        0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
        );

INSERT INTO parametersAdjustFilterImg (
    name,

    FilterColor_Red_Min,
    FilterColor_Red_Max,
    FilterColor_Green_Min,
    FilterColor_Green_Max,
    FilterColor_Blue_Min,
    FilterColor_Blue_Max,

    DefinedAreaForFilter_init_X,
    DefinedAreaForFilter_init_Y,

    FilterInterations_Erode,
    FilterInterations_Dilate,

    SpliceLineJumpWhiteVer_JumpSize_Min,
    SpliceLineJumpWhiteVer_JumpSize_Max,

    SpliceLineJumpWhiteVer_JumpSize_Field_X,
    SpliceLineJumpWhiteVer_JumpSize_Field_Y,

    SpliceLineJumpWhiteHor_JumpSize_Min,
    SpliceLineJumpWhiteHor_JumpSize_Max,

    SpliceLineJumpWhiteHor_JumpSize_Field_X,
    SpliceLineJumpWhiteHor_JumpSize_Field_Y,

    SpliceLineJumpBlackVer_JumpSize_Min,
    SpliceLineJumpBlackVer_JumpSize_Max,

    SpliceLineJumpBlackVer_JumpSize_Field_X,
    SpliceLineJumpBlackVer_JumpSize_Field_Y,

    SpliceLineJumpBlackHor_JumpSize_Min,
    SpliceLineJumpBlackHor_JumpSize_Max,

    SpliceLineJumpBlackHor_JumpSize_Field_X,
    SpliceLineJumpBlackHor_JumpSize_Field_Y,

    FoundObjectSizeFilter_Min,
    FoundObjectSizeFilter_Max,

    VerticalLineSizeFilterOfFoundObject_Min,
    VerticalLineSizeFilterOfFoundObject_Max,

    HorizontalLineSizeFilterOfFoundObject_Min,
    HorizontalLineSizeFilterOfFoundObject_Max,

    parameter01,
    parameter02,
    parameter03,
    parameter04,
    parameter05,
    parameter06,
    parameter07,
    parameter08,
    parameter09,
    parameter10,

    ConstResolutionPixelMm_X,
    ConstResolutionPixelMm_Y,

    parameterReal01,
    parameterReal02,
    parameterReal03,
    parameterReal04,
    parameterReal05,
    parameterReal06,
    parameterReal07,
    parameterReal08
) VALUES (
    'renan',

    0,
    255,
    0,
    255,
    0,
    255,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,

    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,

    0.0,
    0.0,

    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0
);

CREATE TABLE IF NOT EXISTS `historyProductionParametersAdjustFilterImg`(
    id          CHAR(150),
    name        CHAR(50), 
    parameter01 INT,
    parameter02 INT,
    parameter03 INT,
    parameter04 INT,
    parameter05 INT,
    parameter06 INT,
    parameter07 INT,
    parameter08 INT,
    parameter09 INT,
    parameter10 INT,
    parameter11 INT,
    parameter12 INT,
    parameter13 INT,
    parameter14 INT,
    parameter15 INT,
    parameter16 INT,
    parameter17 INT,
    parameter18 INT,
    parameter19 INT,
    parameter20 INT,
    parameterReal01 DECIMAL(15,6),
    parameterReal02 DECIMAL(15,6),
    parameterReal03 DECIMAL(15,6),
    parameterReal04 DECIMAL(15,6),
    PRIMARY KEY(id)
);