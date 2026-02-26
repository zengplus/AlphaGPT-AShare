""" 
 File: config.py
 Date: 2026-01-17
 Description: 全局配置模块。定义了 ModelConfig 类，包含模型训练、数据库连接、硬件设备、交易费率等全局参数配置。
 """ 
import torch
import os

class ModelConfig:
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    DB_URL = f"postgresql://{os.getenv('DB_USER','postgres')}:{os.getenv('DB_PASSWORD','password')}@{os.getenv('DB_HOST','localhost')}:5432/{os.getenv('DB_NAME','crypto_quant')}"
    BATCH_SIZE = 8192
    TRAIN_STEPS = 1000
    MAX_FORMULA_LEN = 12
    TRAIN_USE_OBJECTIVE = True
    TRADE_SIZE_USD = 1000.0
    MIN_LIQUIDITY = 5000.0 # 低于此流动性视为归零/无法交易
    BASE_FEE = 0.005 # 基础费率 0.5% (Swap + Gas + Jito Tip)
    INPUT_DIM = 6
    TOPK = 10
    SIGNAL_LAG = 1
    TURNOVER_PENALTY = 1.0
    ABS_WEIGHT = 0.0
    ALPHA_WEIGHT_BULL = 1.0
    ALPHA_WEIGHT_BEAR = 1.0
    MARKET_REGIME_THRESHOLD = 0.0
    BENCHMARK = "SH000300"
    VALID_MIX_MIN_WEIGHT = 0.7
    VALID_RERANK_TOPN = 64
    VALID_BULL_WEIGHT = 1.0
    VALID_BEAR_WEIGHT = 0.3
    VALID_REWARD_WEIGHT = 0.25
    VALID_REWARD_SCALE = 100.0
    VALID_ENFORCE_BULL_EXCESS = True
    VALID_BULL_EXCESS_MIN_PCT = 0.0
    VALID_ENFORCE_BULL_OBJECTIVE_PASS = True
    VALID_ENFORCE_BEAR_OBJECTIVE_PASS = True
    VALID_REQUIRE_TRAIN_OBJECTIVE_PASS = True
    NEG_EXCESS_PENALTY = 0.0
    NEG_PORT_PENALTY = 0.0
    MIN_EXCESS_WEIGHT = 0.0
    TAIL_SEG_FRACTION = 0.2
    BETA_TARGET = 1.0
    BETA_MIN_BULL = 0.9
    BETA_PENALTY_WEIGHT_BULL = 30.0
    BETA_MIN_PENALTY_WEIGHT_BULL = 60.0
    BETA_PENALTY_WEIGHT_BULL_OBJ = 300.0
    BETA_MIN_PENALTY_WEIGHT_BULL_OBJ = 600.0
    BULL_EXCESS_MIN = 0.0
    BULL_TOTAL_MIN = 0.0
    BEAR_EXCESS_MIN = 0.0
    BEAR_TOTAL_MIN = 0.0
    BULL_EXCESS_TARGET = 0.0
    BULL_EXCESS_HINGE_WEIGHT_SCORE = 0.0
    BULL_EXCESS_HINGE_WEIGHT_OBJ = 5000.0
    TOKEN_LOGIT_BIAS = {"REL_MOM20": 0.6}
