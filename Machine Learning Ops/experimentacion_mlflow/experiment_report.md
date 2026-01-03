
            # Análisis de Experimentos de Predicción de Tarifas de Taxi

            ## Resumen de Resultados
            
            ### Mejor Modelo: xgboost_detailed
            - RMSE: 0.7433
            - R²: 0.9836
            - Mejora sobre el baseline: 11.12%

            ## Comparación de Modelos
            |    | run_name                   |   test_rmse |    test_r2 |   test_mae |   train_test_diff |   execution_time |
|---:|:---------------------------|------------:|-----------:|-----------:|------------------:|-----------------:|
|  0 | xgboost_detailed           |    0.743333 |   0.983568 |   0.276295 |        0.00442617 |        289.911   |
|  1 | random_forest_detailed     |    0.743428 |   0.983564 |   0.269923 |        0.0337745  |       1023.92    |
|  2 | refined_model_detailed     |    0.752455 |   0.983162 |   0.268035 |        0.0544835  |        810.255   |
|  3 | linear_regression_detailed |    0.836299 |   0.979201 |   0.340352 |        0.0455511  |          2.56634 |
|  4 | data_preparation_and_eda   |  nan        | nan        | nan        |        0          |        nan       |

            ## Mejores Hiperparámetros
            ```
            {
  "grid_search_params": "{\"max_depth\": [3, 5], \"learning_rate\": [0.01, 0.1], \"n_estimators\": [100, 200], \"min_child_weight\": [1, 3], \"subsample\": [0.8, 1.0], \"colsample_bytree\": [0.8, 1.0]}",
  "max_depth": "5",
  "min_child_weight": "3",
  "cv_folds": "3",
  "learning_rate": "0.1",
  "early_stopping_rounds": "10",
  "random_state": "42",
  "n_estimators": "100",
  "scoring": "neg_root_mean_squared_error",
  "colsample_bytree": "0.8",
  "subsample": "1.0"
}
            ```

            ## Conclusiones
            1. El modelo xgboost_detailed obtuvo el mejor rendimiento
            2. La diferencia en RMSE entre el mejor y peor modelo es 0.0930
            3. El tiempo de ejecución varió entre 2.57 y 1023.92 segundos
            