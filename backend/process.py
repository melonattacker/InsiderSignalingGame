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
    lr.coef_= np.array([[-0.00811399, -0.0147414, 0.01349019, 0.03293019, 0.00601434, -1.8426328, -0.79240534, -0.10645485, 0.17172625, 1.80135312, 0.79577801, 0.12998358, -0.17681121, -0.19468721, -0.05885516, 0.07327601, -0.12799194, 0.11971723, -0.02095433, 0.11640385, 0.1111035]])
    lr.intercept_ = np.array([2.08857843])
    lr.classes_ = np.array([0, 1])

    test_df = pd.read_csv(path+filename, index_col=0)
    X_test = test_df[['O', 'C', 'E', 'A', 'N', 'dev_con_0to6', 'dev_con_6to12', 'dev_con_12to18', 'dev_con_18to24', 'dev_dis_0to6', 'dev_dis_6to12', 'dev_dis_12to18', 'dev_dis_18to24', 'pc_on_0to6', 'pc_on_6to12', 'pc_on_12to18', 'pc_on_18to24', 'pc_off_0to6', 'pc_off_6to12', 'pc_off_12to18', 'pc_off_18to24']]
    Y_prob = lr.predict_proba(X_test) # 推論
    Y_prob = np.delete(Y_prob, [1], 1)
    test_df['insider_prob'] = np.ravel(Y_prob)
    test_df['insider_prob'] = test_df['insider_prob'].round(5)

    test_df['c_a'] = test_df['authority'].apply(lambda x : 10.0 if x == "Strong" else (7.0 if x == "Normal" else 5.0))
    test_df['v_r'] = test_df['authority'].apply(lambda x : 10.0 if x == "Strong" else (7.0 if x == "Normal" else 5.0))
    test_df['v_w'] = test_df['v_r'].apply(lambda x : x-0.2*x)

    params = {'c_r': 2.5, 'c_rw': 8.0, 'c_w': 1.5, 'c_ww': 7.0}

    # 最適反応を計算
    test_df["best_response"] = test_df.apply(calc_best_response, params=params, axis=1)

    # 不要な列を削除
    test_df = test_df.drop(['c_a', 'v_r', 'v_w', 'O', 'C', 'E', 'A', 'N', 'dev_con_0to6', 'dev_con_6to12', 'dev_con_12to18', 'dev_con_18to24', 'dev_dis_0to6', 'dev_dis_6to12', 'dev_dis_12to18', 'dev_dis_18to24', 'pc_on_0to6', 'pc_on_6to12', 'pc_on_12to18', 'pc_on_18to24', 'pc_off_0to6', 'pc_off_6to12', 'pc_off_12to18', 'pc_off_18to24'], axis=1)

    # ファイルを保存
    filepath = path+"result_"+filename
    test_df.to_csv(filepath)

    return filepath