CREATE DATABASE db_OpenCvRoboXYZDell DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

CREATE TABLE IF NOT EXISTS `AreasOfOperationInTheFilter`(
    id                                          INT NOT NULL AUTO_INCREMENT,
    name                                        CHAR(50),
    Area01_X1                                   INT,
    Area01_Y1                                   INT,
    Area01_X2                                   INT,
    Area01_Y2                                   INT,
    Area02_X1                                   INT,
    Area02_Y1                                   INT,
    Area02_X2                                   INT,
    Area02_Y2                                   INT,
    Area03_X1                                   INT,
    Area03_Y1                                   INT,
    Area03_X2                                   INT,
    Area03_Y2                                   INT,
    Area04_X1                                   INT,
    Area04_Y1                                   INT,
    Area04_X2                                   INT,
    Area04_Y2                                   INT,
    
    PRIMARY KEY(id)
)

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

    SpliceLineJumpWhiteVer_IdAreasOfOperationInTheFilter     INT,

    SpliceLineJumpWhiteHor_JumpSize_Min         INT,
    SpliceLineJumpWhiteHor_JumpSize_Max         INT,

    SpliceLineJumpWhiteHor_IdAreasOfOperationInTheFilter     INT,

    SpliceLineJumpBlackVer_JumpSize_Min         INT,
    SpliceLineJumpBlackVer_JumpSize_Max         INT,

    SpliceLineJumpBlackVer_IdAreasOfOperationInTheFilter     INT,

    SpliceLineJumpBlackHor_JumpSize_Min         INT,
    SpliceLineJumpBlackHor_JumpSize_Max         INT,

    SpliceLineJumpBlackHor_IdAreasOfOperationInTheFilter     INT,

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
        0,
        0,0,
        0,
        0,0,
        0,
        0,0,
        0,
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

    SpliceLineJumpWhiteVer_IdAreasOfOperationInTheFilter,

    SpliceLineJumpWhiteHor_JumpSize_Min,
    SpliceLineJumpWhiteHor_JumpSize_Max,

    SpliceLineJumpWhiteHor_IdAreasOfOperationInTheFilter,

    SpliceLineJumpBlackVer_JumpSize_Min,
    SpliceLineJumpBlackVer_JumpSize_Max,

    SpliceLineJumpBlackVer_IdAreasOfOperationInTheFilter,

    SpliceLineJumpBlackHor_JumpSize_Min,
    SpliceLineJumpBlackHor_JumpSize_Max,

    SpliceLineJumpBlackHor_IdAreasOfOperationInTheFilter,

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