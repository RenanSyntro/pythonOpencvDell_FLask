import cv2
import imutils
import math
import numpy as np
import controllers.adjustmentPanel
import controllers.frames
import controllers.plc
import time
from datetime import datetime
from enum                       import Enum
from services.clearPixelNoise 	import clearPixelLine, clearPixelColum
from rich.console				import Console
from rich.table					import Table

from database.db_insert_historyProductionParametersAdjustFilterImg import db_insert_historyProductionParametersAdjustFilterImg as db

#
#Fonts
#
font = cv2.FONT_HERSHEY_SIMPLEX

#
#Console Print
#
console = Console()

#
#Flag
#
FLag_controllersPlcCP_O_TriggerCamera 	= False
Flag_dateFormated 						= ''

#
#List of coordinate Partial
#
listCoordinatePartial 	= []

#
#Comunication PLC
#
#controllers.plc.comunicationPlc()

def detect_motion():
	print("thread detect_motion chamada")

	def convertPixelToMm_X(pxX):
		#Com variacao de altura do robo ajusta os pixel para continuar na unidade de mm
		#Em 300mmm o cada 0.83 pix representa 1mm
		if (controllers.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X <= 0):
			valorPixel =  controllers.plc.CP_I_DistanceBetweenCameraAndObject * 0.83 / 300  
			return pxX * valorPixel
		else:
		#Este retorno abaixo indica um valor statico independento do eixo Z
			return pxX * controllers.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_X
	

	def convertPixelToMm_Y(pxY):
		#Com variacao de altura do robo ajusta os pixel para continuar na unidade de mm
		#Em 300mmm o cada 0.83 pix representa 1mm
		if (controllers.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y <= 0):
			valorPixel = controllers.plc.CP_I_DistanceBetweenCameraAndObject * 	0.83 / 300  
			return pxY * valorPixel
		else:
		#Este retorno abaixo indica um valor statico independento do eixo Z
			return pxY * controllers.adjustmentPanel.varTrackbar_ConstResolutionPixelMm_Y
		
	def convertMmToPixel_X(mmX):
		return mmX / 2.08333
	

	def convertMmToPixel_Y(mmY):
		return mmY / 2.10937 	


	def convertPixelToMm(Px):
		return Px * 1.0
	

	def convertMmToPixel(mm):
		return mm / 1.0


	def calculateGreatestLineDistanceInRectangle(retangulo):
		coordenadas_x = [ponto[0] for ponto in retangulo]
		coordenadas_y = [ponto[1] for ponto in retangulo]
		distancia_x = max(coordenadas_x) - min(coordenadas_x)
		distancia_y = max(coordenadas_y) - min(coordenadas_y)
		return distancia_x, distancia_y


	def calcular_inclinacao(retangulo):

		reta01 = [retangulo[0], retangulo[1]]

		x1, y1 = reta01[0]
		x2, y2 = reta01[1]

		return (y2 - y1) / (x2 - x1)


	def checkingBoxSize(boxYellow, topAndBottomLine, sideLine, range):

		lineX , lineY = calculateGreatestLineDistanceInRectangle(boxYellow)

		withinRange = (( 		lineX <= topAndBottomLine + range) 
						and (	lineX >= topAndBottomLine - range) 
						and (	lineY <= sideLine + range) 
						and (	lineY >= sideLine - range) 
						)

		return withinRange, lineX, lineY


	def findTheCenter(forma_geometrica):
		soma_x = 0
		soma_y = 0

		for ponto in forma_geometrica:
			soma_x += ponto[0]
			soma_y += ponto[1]

		centro_x = int(soma_x / len(forma_geometrica))
		centro_y = int(soma_y / len(forma_geometrica))

		return centro_x, centro_y


	def orderCoordenates():
		listCoordinatePartial.sort()


	def save_image(frame01 ,frame02, frame03):
		current_dateTime = datetime.now()
		dateFormated = current_dateTime.utcnow().strftime('%d_%m_%Y_%H_%M_%S_%f')[:-3]

		global Flag_dateFormated
		if (dateFormated != Flag_dateFormated):
			Flag_dateFormated = dateFormated
			db.salvar(dateFormated)
			cv2.imwrite(f'images/{dateFormated}_F01.png', frame01)
			cv2.imwrite(f'images/{dateFormated}_F02.png', frame02)
			cv2.imwrite(f'images/{dateFormated}_F03.png', frame03)


	def dibujar(frame01 ,frame02, frame03, color):
		listCoordinatePartial.clear()
		controllers.plc.Id_Det 	= 0

		contornos = cv2.findContours(frame02.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] 
		counterContornos = 0

		for contorno in contornos:
			area = cv2.contourArea(contorno)
			counterContornos = counterContornos + 1

			if len(contorno) > 0:
				if (
						area > controllers.adjustmentPanel.varTrackbar_TamMin 
					and area < controllers.adjustmentPanel.varTrackbar_TamMax):
					    
					rectYellow 	= cv2.minAreaRect(contorno)
					boxYellow 	= cv2.boxPoints(rectYellow)  
					boxYellow 	= np.int0(boxYellow)

					if(
						controllers.adjustmentPanel.varTrackbar_LineHorizontal 	> 0 
						and controllers.adjustmentPanel.varTrackbar_LineVertical > 0 
						and controllers.adjustmentPanel.varTrackbar_LineRange > 0):

						checkingBoxSize_r_withinRange, withinRange_r_line01, withinRange_r_line02 = checkingBoxSize(
							boxYellow,
							controllers.adjustmentPanel.varTrackbar_LineHorizontal,
							controllers.adjustmentPanel.varTrackbar_LineVertical,
							controllers.adjustmentPanel.varTrackbar_LineRange)
						
						if (checkingBoxSize_r_withinRange):
							mmX = 0
							mmY = 0

							x, y = findTheCenter(boxYellow)
							
							#Console.print("X{:0>2}/Y{:0>2}".format(x, y))
							
							cv2.circle(frame03,(x,y),7,(0,255,0),-1)
							cv2.drawContours(frame03, [boxYellow], 0, (0, 255, 255), 2) #cv2.drawContours(frame, [boxYellow], 0, (0, 255, 255), -1)

							px = x - 200
							py = y - 200
							mmX = convertPixelToMm_X(px)
							mmY = convertPixelToMm_Y(py)

							controllers.plc.Id_Det += 1

							cv2.putText(frame03,
										'IdD{:0>2}'.format(controllers.plc.Id_Det),
										(x-30,y-20), font, 0.35,(255,0,255),1,cv2.LINE_AA)
							
							cv2.putText(frame03,
		   								'cX{:.2f}/cY{:.2f}'.format(mmX,mmY),
										(x-30,y-10), font, 0.35,(0,255,0),1,cv2.LINE_AA)
							
							mmL1 = convertPixelToMm_X(withinRange_r_line01)	
							mmL2 = convertPixelToMm_Y(withinRange_r_line02)
							
							cv2.putText(frame03, 'lX{:.2f}/lY{:.2f}'.format(mmL1,	mmL2), (x-30,y+10), font, 0.35,(0,0,255),1,cv2.LINE_AA)
							
							inclinacao = calcular_inclinacao(boxYellow)

							cv2.putText(frame03,
		   								'g{:.2f}'.format(inclinacao),
										(x-20,y+20), font, 0.35,(0,0,255),1,cv2.LINE_AA)

							mmRobo_X = (mmX + controllers.plc.HMI_O_AR_AxisCommandPos_01)
							mmRobo_Y = (mmY + controllers.plc.HMI_O_AR_AxisCommandPos_02 )

							cv2.putText(frame03,
		   								'rX{:.2f}/rY{:.2f}'.format(	mmRobo_X ,mmRobo_Y),
										(x-10,y+30), font, 0.35,(255,0,255),1,cv2.LINE_AA)

							listCoordinatePartial.append([
								mmRobo_X,
				     			mmRobo_Y,
								mmX, 	
								mmY, 
								px,
								py, 
								controllers.plc.Id_trigger,
								controllers.plc.Id_Det])

					else:
						MYellow = cv2.moments(contorno)
						x = int(MYellow["m10"] / MYellow["m00"])
						y = int(MYellow["m01"] / MYellow["m00"])
						cv2.circle(frame03,(x,y),7,(0,255,0),-1)
						cv2.drawContours(frame03, [boxYellow], 0, (0, 255, 255), 2)
						checkingBoxSize_r_withinRange, withinRange_r_line01, withinRange_r_line02 = checkingBoxSize(
							boxYellow,
							controllers.adjustmentPanel.varTrackbar_LineHorizontal,
							controllers.adjustmentPanel.varTrackbar_LineVertical,
							controllers.adjustmentPanel.varTrackbar_LineRange)

						#cv2.putText(frame01,
		   				#					'cX{:.2f}}/cY{:.2f}'.format(x,y),
						#								(x+10,y), font, 0.35,(0,255,0),1,cv2.LINE_AA)
						
						cv2.putText(frame03, 
		  							'lX{:.2f}/lY{:.2f}'.format(withinRange_r_line01,withinRange_r_line02),
									(x+10,y+15), font, 0.35,(0,0,255),1,cv2.LINE_AA
						)


						listCoordinatePartial.append([x,y])

		global FLag_controllersPlcCP_O_TriggerCamera
		if (not controllers.plc.CP_O_TriggerCamera):
			if (FLag_controllersPlcCP_O_TriggerCamera):
				print('FLag_controllersPlcCP_O_TriggerCamera = false')

			FLag_controllersPlcCP_O_TriggerCamera = False
			
		
		if (
			controllers.plc.CP_O_TriggerCamera
			and not controllers.plc.CP_I_TriggerCamera_Return_OK
			and not FLag_controllersPlcCP_O_TriggerCamera
			):

				print('Entrou na sequencia')
				print(FLag_controllersPlcCP_O_TriggerCamera)

				if (len(listCoordinatePartial) <= 0
					and controllers.plc.subSequence_ImageAnalysis_Step == 15):
					print('DM - #01 Executando processo TriggerCamera - Falha Nenhum gabinete encontrado')
					controllers.plc.Write_Fault(2) 

				controllers.plc.Id_trigger	+= 1
				
				print('DM - #01 Executando processo TriggerCamera')
				orderCoordenates()

				print('DM - #01 (Lista Ordenada)')
				print(listCoordinatePartial)
				controllers.plc.ListCoordenate(listCoordinatePartial)

				print('DM - #01 Trigger camera return OK')
				controllers.plc.Write_TriggerReturnOK()
				controllers.plc.CP_I_TriggerCamera_Return_OK 	= True

				FLag_controllersPlcCP_O_TriggerCamera 			= True

				save_image(frame01 ,frame02, frame03)

	while(True):
		print('Tentando conectar webcam')
		cap = cv2.VideoCapture(0)
		time.sleep(1)

		if (cap.isOpened()):
			console.print("Conectado com webcam", style="green on black")

		while cap.isOpened():
			ret, frame03 = cap.read()
			if(ret):
				#frame = cv2.flip(frame, -1)

				#frame_dibujar 		= frame.copy()
				#frame = cv2.imread("./testeCut.jpg")
				
				l_h = controllers.adjustmentPanel.varTrackbar1
				l_s = controllers.adjustmentPanel.varTrackbar2
				l_v = controllers.adjustmentPanel.varTrackbar3
				u_h = controllers.adjustmentPanel.varTrackbar4
				u_s = controllers.adjustmentPanel.varTrackbar5
				u_v = controllers.adjustmentPanel.varTrackbar6

				lower = np.array([l_h, l_s, l_v])
				upper = np.array([u_h, u_s, u_v])

				frame03 	= imutils.resize(frame03, 		width=400, height=400)
				frame03 	= cv2.erode(frame03, 
									None, 
									iterations = controllers.adjustmentPanel.varTrackbar_iterations_erode)
				#hsv 	= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				frame01 	= cv2.inRange(frame03, lower, upper)
				#result 	= cv2.bitwise_and(frame, frame, mask=mask)

				#camada_erode = cv2.erode(mask, None, iterations=0)
				#camada_dilate = cv2.dilate(mask, None, iterations=0)

				cutLine = cv2.cvtColor(frame01, cv2.COLOR_BGR2RGB)
				clearPixelLine.cutLineBySize(cutLine, 
												controllers.adjustmentPanel.varTrackbar_TamMinLv, 
												controllers.adjustmentPanel.varTrackbar_TamMaxLv)
				clearPixelColum.cutColumBySize(cutLine, 
												controllers.adjustmentPanel.varTrackbar_TamMinLh, 
												controllers.adjustmentPanel.varTrackbar_TamMaxLh)
				
				frame02 = cv2.cvtColor(cutLine, cv2.COLOR_BGR2GRAY)
				dibujar(frame01, frame02, frame03, (255,0,0)) #mask

				controllers.frames.changeState_outputVideoLayer01(frame01)
				controllers.frames.changeState_outputVideoLayer02(frame02)
				controllers.frames.changeState_outputVideoLayer03(frame03)
				# controllers.frames.changeState_outputVideoLayer04(noneFrame)
				# controllers.frames.changeState_outputVideoLayer05(noneFrame)

				key = cv2.waitKey(5)
				if key == 27: # ESC
					break
			else:
				cap.release()

				frame03 	= cv2.imread("C:/Users/renan/Desktop/ComputerVision04/pythonOpenCvHtml_InitDell_5032/src/controllers/404.jpg")
				controllers.frames.changeState_outputVideoLayer01(frame03)
				controllers.frames.changeState_outputVideoLayer02(frame03)
				controllers.frames.changeState_outputVideoLayer03(frame03)
				controllers.plc.Write_Fault(1)

		console.print("Can't receive frame (stream end?). Exiting ...", style="green on black")
