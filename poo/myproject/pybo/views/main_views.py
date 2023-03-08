# 메인화면 구성
from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect
import subprocess
from datetime import datetime
from pybo import db
import json
import os, sys


# from sys import path
# path.append("C:/Users/rltmdals/poo/myproject/stt_1")
# from stt import Record_api

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list[:3]
    return render_template('stt_record.html', question_list=question_list)

@bp.route('/start-record/', methods=['GET'])
def start_record():
    from sys import path
    
    path.append("../myproject/stt_1")
    from stt import Record_api
    print ('I got clicked!')
    a_result = Record_api()
    print(a_result)

    path.append("../myproject/processing")
    from station_processing import text_precessing, str_indexing
    # a_result = '서울역 상행 열차 시간 알려줘'
    # a_result = '종로오가역 하행 열차 시간 알려줘'
    # a_result = '가산디지털단지역 사당행 열차 시간 알려줘'

    try:
        answer = text_precessing(a_result)
        # answer= '종로5가역 하행 열차 시간 알려줘'
        station, direction = str_indexing(answer)
        # station, direction = 종로5가, 하행

        path.append("../myproject/output_result")
        from total import output_keyvlaue
        response = output_keyvlaue(station, direction)

        db_answer = Question(input=a_result, station=station, direction=direction, create_date=datetime.now())
        db.session.add(db_answer)
        db.session.commit()

        print('1: ', response)
        third = response[1]
        print(third)

        return response

    except:
        # a_result = '서울역 사당 열차 시간 알려줘' or '서울 사당 열차 시간 알려줘'
        except_result = f"{answer} 로 인식되었습니다"
        db_answer = Question(input=a_result, create_date=datetime.now())
        db.session.add(db_answer)
        db.session.commit()
        response = except_result
        

        return response
    
    # finally:

@bp.route('/start-gara/', methods=['GET'])
def start_gara():
    from sys import path

    path.append("../myproject/processing")
    from station_processing import text_precessing, str_indexing
    a_result = '서울역 상행 열차 시간 알려줘'
    # a_result = '종로오가역 하행 열차 시간 알려줘'
    # a_result = '가산디지털단지역 사당행 열차 시간 알려줘'

    try:
        answer = text_precessing(a_result)
        # answer= '종로5가역 하행 열차 시간 알려줘'
        station, direction = str_indexing(answer)
        # station, direction = 종로5가, 하행

        path.append("../myproject/output_result")
        from total import output_keyvlaue
        response = output_keyvlaue(station, direction)

        db_answer = Question(input=a_result, station=station, direction=direction, create_date=datetime.now())
        db.session.add(db_answer)
        db.session.commit()

        print('1: ', response)
        third = response[1]
        print(third)

        return response

    except:
        # a_result = '서울역 사당 열차 시간 알려줘' or '서울 사당 열차 시간 알려줘'
        except_result = f"{answer} 로 인식되었습니다"
        db_answer = Question(input=a_result, create_date=datetime.now())
        db.session.add(db_answer)
        db.session.commit()
        response = except_result
        

        return response

