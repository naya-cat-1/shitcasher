import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 读取数据集
file_path_climate = 'climate_change_indicators.csv'
df_climate = pd.read_csv(file_path_climate)

# 提取特定国家（印度）的年度温度变化数据
df_india = df_climate[df_climate['Country'].str.contains('India', case=False)]
india_temp_changes = df_india.loc[:, 'F1961':'F2022'].transpose()
india_temp_changes.columns = ['Temperature Change']
india_temp_changes.index = pd.date_range(start='1961', periods=len(india_temp_changes), freq='Y')

# 准备时间序列数据
temp_series = india_temp_changes['Temperature Change'].reset_index(drop=True)

# 选择ARIMA模型参数
p, d, q = 5, 1, 0

# 拟合ARIMA模型
model = ARIMA(temp_series, order=(p, d, q))
model_fit = model.fit()

# 进行未来5年的预测
forecast_years = 5
forecast = model_fit.forecast(steps=forecast_years)

# 绘制历史数据和预测数据
forecast_years_index = pd.date_range(start='2023', periods=forecast_years, freq='Y')
forecast_series = pd.Series(forecast, index=forecast_years_index)

plt.figure(figsize=(12, 6))
plt.plot(india_temp_changes.index, temp_series, label='Historical Annual Temperature Change')
plt.plot(forecast_series.index, forecast_series, label='Forecasted Annual Temperature Change', color='red')
plt.title('Annual Temperature Change in India and Forecast')
plt.xlabel('Year')
plt.ylabel('Temperature Change (°C)')
plt.legend()
plt.show()
