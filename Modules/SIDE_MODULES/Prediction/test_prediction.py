from Modules.SIDE_MODULES.Prediction.value_time_prediction import Prediction

if __name__ == '__main__':
    p = Prediction(0.00001, 4000000, "USA", "total_cases")

    # get the proceeded data:
    data = p.define_numpy()

    # get the new dates:
    number_days = p.get_days(["2020", "12", "01"])
    new_dates = [i for i in range(len(data[0]))]
    dates_to_predict = [i + len(new_dates) for i in range(number_days[2] + 1)]

    av_prediction_score = 0
    # predict:
    for i in range(len(number_days[1])):
        pred = p.prediction(new_dates, data[1], [dates_to_predict[i]])
        av_prediction_score = p.pred_score
    print("Average prediction score = {}%".format(round(av_prediction_score * 100, 3)))
