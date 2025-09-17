from flask import Blueprint, render_template, request, jsonify
from app.agents.evaluator_optimizer_agent import EvaluatorOptimizerAgent
from app.agents.memory_augmented_agent import MemoryAugmentedAgent

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.get_json()
    topic = data.get('topic')
    agent = EvaluatorOptimizerAgent()
    quiz = agent.execute(topic)
    return jsonify({'quiz': quiz})

@main_blueprint.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.get_json()
    student_id = data.get('student_id')
    agent = MemoryAugmentedAgent(student_id)
    recommendation = agent.execute()
    return jsonify({'recommendation': recommendation})

@main_blueprint.route('/update_performance', methods=['POST'])
def update_performance():
    data = request.get_json()
    student_id = data.get('student_id')
    topic = data.get('topic')
    score = data.get('score')
    agent = MemoryAugmentedAgent(student_id)
    agent.update_performance(topic, score)
    return jsonify({'status': 'success'})