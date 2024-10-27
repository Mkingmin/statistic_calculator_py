import numpy as np

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    else:
        valid_list=np.array(list).reshape(3,3)
        mean_values=[(np.mean(valid_list, axis=0).tolist()), (np.mean(valid_list, axis=1).tolist()), (valid_list.flatten().mean())]
        variance_values=[(np.var(valid_list, axis=0).tolist()), (np.var(valid_list, axis=1).tolist()), (valid_list.flatten().var())]
        std_values=[(np.std(valid_list, axis=0).tolist()), (np.std(valid_list, axis=1).tolist()), (valid_list.flatten().std())]
        max_values=[(np.max(valid_list, axis=0).tolist()), (np.max(valid_list, axis=1).tolist()), (valid_list.flatten().max())]
        min_values=[(np.min(valid_list, axis=0).tolist()), (np.min(valid_list, axis=1).tolist()), (valid_list.flatten().min())]
        sum_values=[(np.sum(valid_list, axis=0).tolist()), (np.sum(valid_list, axis=1).tolist()), (valid_list.flatten().sum())]

        calculations={"mean": mean_values,
                      "variance": variance_values,
                      "standard deviation": std_values,
                      "max": max_values,
                      "min": min_values,
                      "sum": sum_values}

    return calculations