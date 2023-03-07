# 메인화면 구성
from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect
import subprocess
from datetime import datetime
from pybo import db
import json


# from sys import path
# path.append("C:/Users/rltmdals/poo/myproject/stt_1")
# from stt import Record_api

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list[:3]
    # 3개만 나오게 처리
    return render_template('stt_record.html', question_list=question_list)


@bp.route('/start-record/', methods=['GET'])
def start_record():
    input_list = []

    from sys import path
    # audio 넣는 부분 나중에 주석풀기
    # path.append("C:/Users/rltmdals/poo/myproject/stt_1")
    # from stt import Record_api
    
    # print ('I got clicked!')
    # # Record_api()
    # a = Record_api.res.json()
    # # print(a)
    # analysisResult_json = a.get('analysisResult')
    # a_result = analysisResult_json.get('result')
    # # result_sentence = f"<{a_result}>\n 결과가 맞으십니까?"

    path.append("./processing")
    from station_processing import text_precessing, str_indexing
    a_result = '종로오가역 하행 열차 시간 알려줘'
    # a_result = '종로오가역 하행 열차 시간 알려줘'

    answer = text_precessing(a_result)
    # answer= '종로5가역 하행 열차 시간 알려줘'

    station, direction = str_indexing(answer)
    # station, direction = 종로5가, 하행

    path.append("./output_result")
    from total import output_keyvlaue
    response = output_keyvlaue(station, direction)

    db_answer = Question(input=a_result, station=station, direction=direction, create_date=datetime.now())
    db.session.add(db_answer)
    db.session.commit()

    return response