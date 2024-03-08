from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)