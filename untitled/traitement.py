from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


# # https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html
# def svmmethode(failure, fedu, schoolsup, medu, goout, freetime):
#     model = SVC(gamma="scale", C=1.44, kernel="poly")
#     data_for_svm = pd.read_csv('data/data_for_svm.csv')
#     target_for_svm = pd.read_csv('data/target_for_svm.csv')
#     new_row = {'failures': [failure], 'Fedu': [fedu], 'schoolsup': [schoolsup], 'Medu': [medu], 'goout': [goout],
#                'freetime': [freetime]}

#     my_row_df = pd.DataFrame(new_row, columns=['failures', 'Fedu', 'schoolsup', 'Medu', 'goout', 'freetime'],
#                              dtype='int64')

#     data_for_svm.loc[len(data_for_svm)] = my_row_df.loc[0]

#     column_names_for_one_hot = data_for_svm.columns[0:]
#     underMI_20_dummy_codding = pd.get_dummies(data_for_svm, columns=column_names_for_one_hot, drop_first=True)
#     my_row = underMI_20_dummy_codding.tail(1)
#     underMI_20_dummy_codding.drop(my_row.index, inplace=True)

#     model.fit(underMI_20_dummy_codding, target_for_svm)
#     result = model.predict(my_row)
#     # do something with the book
#     return result


# def mlpmethode(failure, fedu, schoolsup, medu, goout, freetime):
#     model = MLPClassifier(batch_size=350, activation="logistic", early_stopping=False, learning_rate="invscaling",
#                           momentum=0.633)
#     data_for_mlp = pd.read_csv('data/data_for_mlp.csv')
#     target = pd.read_csv('data/target.csv')
#     new_row = {'failures': [failure], 'Fedu': [fedu], 'schoolsup': [schoolsup], 'Medu': [medu], 'goout': [goout],
#                'freetime': [freetime]}

#     my_row_df = pd.DataFrame(new_row, columns=['failures', 'Fedu', 'schoolsup', 'Medu', 'goout', 'freetime'],
#                              dtype='int64')

#     data_for_mlp.loc[len(data_for_mlp)] = my_row_df.loc[0]

#     column_names_for_onehot = data_for_mlp.columns[0:]
#     overMI_20_dummy_codding = pd.get_dummies(data_for_mlp, columns=column_names_for_onehot, drop_first=True)
#     my_row = overMI_20_dummy_codding.tail(1)
#     overMI_20_dummy_codding.drop(my_row.index, inplace=True)

#     model.fit(overMI_20_dummy_codding, target)
#     result = model.predict(my_row)
#     # do something with the book
#     return result


def knnmethode(Medu, Fedu, famrel, freetime, goout, Walc, health, Age, Absences, Mjob, Fjob, reason):
    model = KNeighborsClassifier(n_neighbors=2, weights='distance', metric='hamming')
    data_for_knn = pd.read_csv('data/data_for_knn.csv')
    target = pd.read_csv('data/target_for_knn.csv')
    new_row = {'Medu': [Medu], 'Fedu': [Fedu], 'famrel': [famrel], 'freetime': [freetime], 'goout': [goout],
               'Walc': [Walc],
               'health': [health], 'Age': [Age], 'Absences': [Absences], 'Mjob': [Mjob], 'Fjob': [Fjob],
               'reason': [reason]}

    my_row_df = pd.DataFrame(new_row, columns=['Medu', 'Fedu', 'famrel', 'freetime', 'goout', 'Walc', 'health', 'Age',
                                               'Absences', 'Mjob', 'Fjob', 'reason'],
                             dtype='int64')

    model.fit(data_for_knn, target)
    result = model.predict(my_row_df)
    # do something with the book
    return result


def cartmethode(failures, Fedu, schoolsup, Medu, goout, freetime):
    model = DecisionTreeClassifier(max_depth=2, max_features=5, min_samples_leaf=5, splitter='best')
    data_for_knn = pd.read_csv('data/data_for_cart.csv')
    target = pd.read_csv('data/target_for_cart.csv')
    new_row = {'failures': [failures], 'Fedu': [Fedu], 'schoolsup': [schoolsup], 'Medu': [Medu], 'goout': [goout],
               'freetime': [freetime]}

    my_row_df = pd.DataFrame(new_row, columns=['failures', 'Fedu', 'schoolsup', 'Medu', 'goout', 'freetime'],
                             dtype='int64')

    model.fit(data_for_knn, target)
    result = model.predict(my_row_df)
    # do something with the book
    return result
