#!/usr/bin/env python
# coding: utf-8

# In[74]:


class Solution:
     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 1단계: day별 최소 ticket 가격을 저장한 list 생성
        day_size = max(days)                
        cost_point = costs[0] * day_size   # list 생성 시 입력할 초기값
        dp = [0] + [cost_point] * day_size # 각 인덱스를 날짜로 하기 위해서 인덱스 0에는 0을 추가 

        # 2단계: list별로 ticket 
        duration_day = [1, 7, 30]

        for day in range(1, day_size + 1):
            if day not in days: 
                dp[day] = dp[day - 1] # when day no in days(이전 날짜의 티겟 가격과 동일ㅇ)
                continue
            else: # when i in days (calcuating)
                dp[day] = min(costs[0] + dp[max(0, day-1)], costs[1] + dp[max(0, day-7)], costs[2] + dp[max(0, day-30)])         

        return dp[-1]

