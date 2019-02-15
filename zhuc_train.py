# -*- coding:utf-8 -*-
import time
from options.train_options import TrainOptions
from data import CreateDataLoader
from models import create_model

if __name__ == '__main__':
    opt = TrainOptions().parse()
    data_loader = CreateDataLoader(opt)

    tmp = 0