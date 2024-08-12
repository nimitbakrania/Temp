def UW():
    columns = ['Name', 'Blue', 'Spread', 'Flag', 'End_Spread', 'End_Exp',
           'Take_Profit', 'Total_Num', 'Win_Ratio', 'Avg_Time',
           'Max_Drawdown', 'Cum_PNL', 'Average_PNL', 'Max_PNL', 'Time_Stop', 'Fourier', 'ttof']

    # Create an empty DataFrame
    main = pd.DataFrame(columns=columns)
    for i in l:
        a = i[0]
        b = i[1]
        try:
            date,x,y = readdata('DataFinal.csv',date=0,inp_1=a,inp_2=b) 
            name = str(crossrates.columns[a]) + ' ' + str(crossrates.columns[b])
            name1 = str(crossrates.columns[a])
            name2 = str(crossrates.columns[b])
            print(name)
            print(a,b)
            here,back_time, max_pnl, time_stop,df_save, ema, flag_ibg, end_of_spread, end_of_exp, take_prof, total_num, win_ratio,avg_time, max_drawdown, cum_pnl, avg_pnl = back_test_RV(date,x,y,window=30,com=30,entry_z=2.5,maxentry_z=7,stoploss_z=10,takeprofit_z=0,instrument='swap',pca=False,verbose=False, weightthres_1 = [0.3, 1.5], weight_override = [1,1]) #weightthres_1 = [minimum entry weight, maximum entry weight]  
            if here and (win_ratio > 79.0):
                ema_list = ema.tolist()
                dfs = df_save.tolist()
                country_1 = excel_country[a-1]
                country_2 = excel_country[b-1]
                fname = ("Receive "+ name1 + ", Pay: " + name2) if flag_ibg else ("Receive "+ name2 + ", Pay: " + name1)
                fourier, ttof = find_nearest_business_day(back_time, country_1, country_2, math.ceil(float(avg_time)))
                data = {
                    'Name': fname,
                    'Win_Ratio': win_ratio,
                    'Blue': (dfs,),
                    'Spread': (ema_list,),
                    'Flag': flag_ibg,
                    'End_Spread': end_of_spread*100,
                    'End_Exp': end_of_exp,
                    'Take_Profit': take_prof*100,
                    'Total_Num': total_num,
                    'Avg_Time': avg_time,
                    'Max_Drawdown': max_drawdown,
                    'Cum_PNL': cum_pnl,
                    'Average_PNL': avg_pnl, 
                    'Max_PNL':max_pnl*100, 
                    'Time_Stop':time_stop,
                    'Fourier': fourier,
                    'ttof': ttof
                }
                main.loc[len(main.index)] = data
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        except:
            print('Error')
            print(a,b)
    
    return main

def MT():
    columns = ['Name', 'Blue', 'Spread', 'Flag', 'End_Spread', 'End_Exp',
           'Take_Profit', 'Total_Num', 'Win_Ratio', 'Avg_Time',
           'Max_Drawdown', 'Cum_PNL', 'Average_PNL', 'Max_PNL', 'Time_Stop', 'Fourier', 'ttof']

    main = pd.DataFrame(columns=columns)
    for i in l:
        a = i[0]
        b = i[1]
        try:
            date,x,y = readdata('DataFinal.csv',date=0,inp_1=a,inp_2=b) 
            name = str(crossrates.columns[a]) + ' ' + str(crossrates.columns[b])
            name1 = str(crossrates.columns[a])
            name2 = str(crossrates.columns[b])
            print(name)
            print(a,b)
            here,back_time, max_pnl, time_stop,df_save, ema, flag_ibg, end_of_spread, end_of_exp, take_prof, total_num, win_ratio,avg_time, max_drawdown, cum_pnl, avg_pnl = back_test_RV(date,x,y,window=90,com=30,entry_z=3,maxentry_z=7,stoploss_z=10,takeprofit_z=-3,instrument='swap',pca=False,verbose=False, weightthres_1 = [0.3, 1.5], weight_override = [1,1])
            if here and (win_ratio > 79.0):
                ema_list = ema.tolist()
                dfs = df_save.tolist()
                country_1 = excel_country[a-1]
                country_2 = excel_country[b-1]
                fname = ("Receive "+ name1 + ", Pay: " + name2) if flag_ibg else ("Receive "+ name2 + ", Pay: " + name1)
                fourier, ttof = find_nearest_business_day(back_time, country_1, country_2, math.ceil(float(avg_time)))
                data = {
                    'Name': fname,
                    'Win_Ratio': win_ratio,
                    'Blue': (dfs,),
                    'Spread': (ema_list,),
                    'Flag': flag_ibg,
                    'End_Spread': end_of_spread*100,
                    'End_Exp': end_of_exp,
                    'Take_Profit': take_prof*100,
                    'Total_Num': total_num,
                    'Avg_Time': avg_time,
                    'Max_Drawdown': max_drawdown,
                    'Cum_PNL': cum_pnl,
                    'Average_PNL': avg_pnl, 
                    'Max_PNL':max_pnl*100, 
                    'Time_Stop':time_stop,
                    'Fourier': fourier,
                    'ttof': ttof
                }
                main.loc[len(main.index)] = data
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        except:
            print('Error')
            print(a,b)
    
    return main