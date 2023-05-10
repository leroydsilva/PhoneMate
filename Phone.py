from flask_restx import Namespace, Resource,fields
from flask import Flask, render_template, request,jsonify
# from mysql import mysql
from models import get_phones


phone_ns=Namespace('phone',description='to fetch phone name with id')

#Model Serializer
Phone_model=phone_ns.model(
    "Phones",
    {
        "Phone_id":fields.Integer(),
        "Phone_name":fields.String(),
        "Phone_price":fields.Integer(),
        "Phone_img" : fields.String(),
        "Screen_size": fields.Float(),
        "RAM"         : fields.String(),
        "Internal_storage":fields.String(),
        "Processor":fields.String(),
        "Rear_camera":fields.String(),
        "Front_camera":fields.String(),
        "Battery"     : fields.Integer(attribute ="Battery_capacity"),
        "fiveg"       : fields.Boolean(),
        "Rating":fields.Integer(attribute="Value_for_Money")


    }
)
# to add strict validation in your api use the below @api.expect is not going to validate

my_resource_parser = phone_ns.parser()
my_resource_parser.add_argument('Camera', type=bool, required=True)
my_resource_parser.add_argument('Storage', type=bool,required=True)
my_resource_parser.add_argument('Usage', type=bool,required=True)
my_resource_parser.add_argument('Game', type=bool,required=True)
my_resource_parser.add_argument('Display', type=bool,required=True)
my_resource_parser.add_argument('Protection', type=bool,required=True)



@phone_ns.route('/Phone/a')
class PhoneResource(Resource):
    @phone_ns.marshal_list_with(Phone_model)
    def get(self):
        cursor = mysql.connect().cursor()
        sql = "SELECT Phone_id,Phone_name,Phone_price FROM Phone"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    @phone_ns.expect(Phone_model)
    def post(self):
        # args=my_resource_parser.parse_args()
        cursor = mysql.connect().cursor()
        data=request.get_json() 
        p=data.get('Table')
        sql = f"SELECT Phone_id,Phone_name,Phone_price FROM {p}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        # data=request.get_json()
        # return jsonify({"message":data.get('Phone_name')})


@phone_ns.route('/Phone/<int:id>')
class PhoneResource(Resource):
    @phone_ns.expect(Phone_model)
    @phone_ns.marshal_with(Phone_model)
    def get(self,id):
        cursor = mysql.connect().cursor()
        sql = f"SELECT * FROM Phone where Phone_id={id}"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

@phone_ns.route('/Phone/',strict_slashes=False)
class PhoneResource(Resource):
    @phone_ns.marshal_with(Phone_model)
    def post(self):
        args = my_resource_parser.parse_args()
        result = get_phones(args)
        return result,201

        # camera = args['Camera']
        # storage = args['Storage']
        # usage = args['Usage']
        # game = args['Game']
        # display = args['Display']
        # protection = args['Protection']

        # phone_query = (
        #     db.session.query(Phone.id, Phone.name, Phone.price, Phone.img)
        #     .join(Rating, Phone.name == Rating.phone_name)
        #     .join(Spec, Phone.name == Spec.phone_name)
        #     .filter(and_(
        #         Rating.camera > (7 if camera else 6),
        #         Spec.internal_storage.like('%128GB%') if storage else True,
        #         Rating.battery_life > 8 if usage else True,
        #         Spec.battery_capacity > 4000 if usage else True,
        #         (
        #             Spec.ram.like('%12GB%')
        #             | Spec.ram.like('%8GB%')
        #             | Spec.processor_make.like('%Apple%')
        #         ) if game else True,
        #         Spec.refresh_rate > 80 if game else True,
        #         Rating.performance > 8 if game else True,
        #         Rating.display > 8 if display else Rating.display > 6,
        #         Rating.design > 8 if protection else True,
        #     ))
        # )
        # phones = phone_query.all()
        # return phones





        # args=my_resource_parser.parse_args()
        # data=request.get_json()
        # cursor = mysql.connect().cursor()
        # if (args['Camera']==True):
        #      Cam="r.Camera >7"
        #      print('*********************')
        # else:
        #      Cam="r.Camera>6"
        # if (args['Storage']==True):
        #      Storage="s.Internal_storage LIKE '%128GB%'"
        # else:
        #      Storage="1=1"   
        # if(args['Usage']):
        #     Battery_life='r.Battery_Life >8'   
        #     Battery_cap='s.Battery_capacity > 4000'    
        # else:
        #     Battery_cap=Battery_life="1=1"
        # if(args['Game']):
        #     Battery_life='r.Battery_Life >8' 
        #     Ram="((s.RAM like '%12GB%' or s.RAM like  '%8GB%') or s.Processor_make LIKE '%Apple%')"
        #     Refresh="s.Refresh_Rate >80"
        #     Performance="r.Performance>8"
        # else:
        #     Performance=Battery_life=Ram=Refresh="1=1"
        # if(args['Display']):
        #     Display='r.Display>8'
        # else:
        #     Display='r.Display>6'
        # if(args['Protection']):
        #     Protection='r.Design >8'
        # else:
        #     Protection='1=1'

        # sql = f'''
        # SELECT
        # p.Phone_id,p.Phone_name,p.Phone_price,p.Phone_img
        # FROM phone p
        # JOIN ratings r
        # ON p.Phone_name = r.Phone_name
        # JOIN specs s
        # ON p.Phone_name = s.Phone_name where {Cam} and {Storage} and {Battery_life} and {Battery_cap} and 
        # {Ram} and {Display} and {Protection} and {Refresh} and {Performance}
        # '''     
        # cursor.execute(sql)
        # results = cursor.fetchall()
        # return results


  