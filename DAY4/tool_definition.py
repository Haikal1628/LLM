from openai import OpenAI
import json

import os


# 1. nama fungsi -> calcullator
# 2. Desc -> panggil des ini kalua mau menggunakan operasi matematika
# 3. Parameters -> parameter apa yagn harus diisi 


basic_template = {
    'type':'function',
    'function':{
        'name':'calculator',
        'description':'ini adalah function_description',
        'parameters':{
            'type':'object',
            'properties':{
                'param1':{
                    'type':'string',
                    'description':'ini adalah param1_description'
                },
                'param2':{
                    'type':'number',
                    'description':'ini adalah number2_description'
                },
                'param3':{
                    'type':'array',
                    'items':{'type':'string'},# bisa diganti typenya
                    'description':'ini adalah param3_description'
                },
                'param4':{
                    'type':'object',
                    # aewalnya items ganti ke properties
                    'properties':{ 
                        'city':{'type':'string'},
                        'zip_code':{'type':'number'}
                    },# bisa diganti typena
                    'description':'ini adalah param4_description'
                }
            },
            'required':['param1','param2','param3','param4']
        }
    }
}



