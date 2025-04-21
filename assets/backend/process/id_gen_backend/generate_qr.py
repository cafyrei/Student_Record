import qrcode

class QRCodeGenerator:
    def generete_qr(self, data: str, filename: str):

        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=1,  # Thickness of the border
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        student_qr = qr.make_image(fill='black', back_color='white')
        student_qr.save(f'assets/img/collection_qr/{filename}.png   ')

        

