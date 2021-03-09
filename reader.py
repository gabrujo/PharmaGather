import barcode
from barcode.writer import ImageWriter

hr= barcode.get_barcode_class('code39')
Hr= hr('MehdiSei1912',writer=ImageWriter())
qr=Hr.save('md')

