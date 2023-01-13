from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from resources.image import FileUploadResource
from resources.posting import PostingResource
from resources.rekognition import ObjectDetectionResource, PhotoRekognitionResource





app = Flask(__name__)

jwt = JWTManager(app)

api = Api(app)
# 경로를 리소스와 연결한다.
api.add_resource(FileUploadResource,'/upload')
api.add_resource(ObjectDetectionResource,'/object_detection')
api.add_resource(PhotoRekognitionResource,'/get_photo_label')
api.add_resource(PostingResource,'/posting')




if __name__ == '__main__' : 
    app.run()