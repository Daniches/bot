from imageai.Detection import ObjectDetection
from modules.base_module import BaseModule

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("modules/image_classificator/yolo.h5")
detector.loadModel()


class ObjectDetection(BaseModule):
    @staticmethod
    def run(update, context):
        file = context.bot.getFile(update.message.photo[1].file_id)
        file.download('image.jpg')
        detections = detector.detectObjectsFromImage(input_image="image.jpg",
                                                     output_image_path="image_result.jpg",
                                                     minimum_percentage_probability=70)
        text = ', '.join([image_object["name"] for image_object in detections])
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('image_result.jpg', 'rb'))

object_detection_module = ObjectDetection()