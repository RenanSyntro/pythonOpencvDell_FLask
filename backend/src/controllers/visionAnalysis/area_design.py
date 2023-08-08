import controllers.varGlobal.global_areas_props as area_global_variable
import cv2

cor_bgr_area_retangulo = (0, 255, 255)
cor_bgr_borda_retangulo = (0, 255, 0)
transparencia = 0.5
espessura_retangulo = 2

def desenhar_area1(frame03):
    x1 = area_global_variable.var_parametersArea_Area01_X1
    y1 = area_global_variable.var_parametersArea_Area01_Y1
    x2 = area_global_variable.var_parametersArea_Area01_X2
    y2 = area_global_variable.var_parametersArea_Area01_Y2
   
    font_scale = 0.4
    try:
        if sum([x1, x2, y1, y2]) < 1:
            font_scale = 0
    except:
        pass

    frame03 = cv2.addWeighted(frame03, 1 - transparencia, cv2.rectangle(frame03.copy(), (x1, y1), (x2, y2), cor_bgr_area_retangulo, -1), transparencia, 0)
    cv2.rectangle(frame03, (x1, y1), (x2, y2), cor_bgr_borda_retangulo, espessura_retangulo)
    cv2.putText(frame03, 'area_1', (x1+5, y1+15), cv2.FONT_HERSHEY_COMPLEX, font_scale, (255, 0, 0), 1, cv2.LINE_AA)
    return frame03



def desenhar_area2(frame03):
    x1 = area_global_variable.var_parametersArea_Area02_X1
    y1 = area_global_variable.var_parametersArea_Area02_Y1
    x2 = area_global_variable.var_parametersArea_Area02_X2
    y2 = area_global_variable.var_parametersArea_Area02_Y2

    font_scale = 0.4
    try:
        if sum([x1, x2, y1, y2]) < 1:
            font_scale = 0
    except:
        pass

    frame03 = cv2.addWeighted(frame03, 1 - transparencia, cv2.rectangle(frame03.copy(), (x1, y1), (x2, y2), cor_bgr_area_retangulo, -1), transparencia, 0)
    cv2.rectangle(frame03, (x1, y1), (x2, y2), cor_bgr_borda_retangulo, espessura_retangulo)
    cv2.putText(frame03, 'area_2', (x1+5, y1+15), cv2.FONT_HERSHEY_COMPLEX, font_scale, (255, 0, 0), 1, cv2.LINE_AA)
    return frame03


def desenhar_area3(frame03):
    x1 = area_global_variable.var_parametersArea_Area03_X1
    y1 = area_global_variable.var_parametersArea_Area03_Y1
    x2 = area_global_variable.var_parametersArea_Area03_X2
    y2 = area_global_variable.var_parametersArea_Area03_Y2

    font_scale = 0.4
    try:
        if sum([x1, x2, y1, y2]) < 1:
            font_scale = 0
    except:
        pass

    frame03 = cv2.addWeighted(frame03, 1 - transparencia, cv2.rectangle(frame03.copy(), (x1, y1), (x2, y2), cor_bgr_area_retangulo, -1), transparencia, 0)
    cv2.rectangle(frame03, (x1, y1), (x2, y2), cor_bgr_borda_retangulo, espessura_retangulo)
    cv2.putText(frame03, 'area_3', (x1+5, y1+15), cv2.FONT_HERSHEY_COMPLEX, font_scale, (255, 0, 0), 1, cv2.LINE_AA)
    return frame03


def desenhar_area4(frame03):
    x1 = area_global_variable.var_parametersArea_Area04_X1
    y1 = area_global_variable.var_parametersArea_Area04_Y1
    x2 = area_global_variable.var_parametersArea_Area04_X2
    y2 = area_global_variable.var_parametersArea_Area04_Y2

    font_scale = 0.4
    try:
        if sum([x1, x2, y1, y2]) < 1:
            font_scale = 0
    except:
        pass

    frame03 = cv2.addWeighted(frame03, 1 - transparencia, cv2.rectangle(frame03.copy(), (x1, y1), (x2, y2), cor_bgr_area_retangulo, -1), transparencia, 0)
    cv2.rectangle(frame03, (x1, y1), (x2, y2), cor_bgr_borda_retangulo, espessura_retangulo)
    cv2.putText(frame03, 'area_4', (x1+5, y1+15), cv2.FONT_HERSHEY_COMPLEX, font_scale, (255, 0, 0), 1, cv2.LINE_AA)
    return frame03

def desenhar_area(frame03):
    desenhar_area1(frame03)
    desenhar_area2(frame03)
    desenhar_area3(frame03)
    desenhar_area4(frame03)
