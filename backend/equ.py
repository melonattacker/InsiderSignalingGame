
def calc_equ(params):
    p_i = params["p_i"]
    c_a = params["c_a"]
    c_r = params["c_r"]
    c_rw = params["c_rw"]
    c_w = params["c_w"]
    c_ww = params["c_ww"]
    v_r = params["v_r"]
    v_w = params["v_w"]

    actions = []
    actions.append((p_i*(-c_r+v_r)+(1-p_i)*(-c_r-c_rw), "Revoke")) # Revoke
    actions.append((p_i*(-c_w+v_w)+(1-p_i)*(-c_w-c_ww), "Warn")) # Warn
    actions.append((p_i*(-c_a), "Keep")) # Keep
    print(actions)
    return max(actions)[1]
