import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

def calc_best_response(row, params):
    c_r = params["c_r"]
    c_rw = params["c_rw"]
    c_w = params["c_w"]
    c_ww = params["c_ww"]
    c_a = row["c_a"]
    v_r = row["v_r"]
    v_w = row["v_w"]
    p_i = row["insider_prob"]

    actions = []
    actions.append((p_i*(-c_r+v_r)+(1-p_i)*(-c_r-c_rw), "Revoke")) # Revoke
    actions.append((p_i*(-c_w+v_w)+(1-p_i)*(-c_w-c_ww), "Warn")) # Warn
    actions.append((p_i*(-c_a), "Keep")) # Keep
    return max(actions)[1]

def process(path, filename):
    # ロジスティック回帰学習済みのパラメータを設定
    lr = LogisticRegression()
    lr.coef_= np.array([[-0.03670863, -0.01998146,  0.01744572,  0.01780376, -0.00202065]])
    lr.intercept_ = np.array([2.08857843])
    lr.classes_ = np.array([0, 1])

    test_df = pd.read_csv(path+filename, index_col=0)
    X_test = test_df[['O', 'C', 'E', 'A', 'N']]
    Y_prob = lr.predict_proba(X_test) # 推論
    Y_prob = np.delete(Y_prob, [1], 1)
    test_df['insider_prob'] = np.ravel(Y_prob)

    test_df['c_a'] = test_df['authority'].apply(lambda x : 10.0 if x == "Strong" else (7.0 if x == "Normal" else 5.0))
    test_df['v_r'] = test_df['authority'].apply(lambda x : 10.0 if x == "Strong" else (7.0 if x == "Normal" else 5.0))
    test_df['v_w'] = test_df['v_r'].apply(lambda x : x-0.2*x)

    params = {'c_r': 2.5, 'c_rw': 8.0, 'c_w': 1.5, 'c_ww': 7.0}

    # 最適反応を計算
    test_df["best_response"] = test_df.apply(calc_best_response, params=params, axis=1)
    # ファイルを保存
    filepath = path+"result_"+filename
    test_df.to_csv(filepath)

    return filepath