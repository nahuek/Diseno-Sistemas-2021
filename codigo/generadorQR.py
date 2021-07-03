import qrcode 
import cv2  
 
class RegistroQR:

    def crear_QR(self, nombre, dni):
        self.data= dni
        self.imagen= nombre +".png"
        QRimage = qrcode.make(self.data)
        QRimage.save(self.imagen)
        print("El QR se genero correctamente")
 

    def leer_QR(self, nombre):
        image = cv2.imread(nombre+".png")
        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        if vertices_array is not None:
            return int(data)
        else:
            print("Ocurrio un error")
