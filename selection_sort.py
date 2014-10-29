#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(arr):
	size = len(arr)
	for i in range(size):
		m = i
		for j in range(i+1,size):
			if arr[j]<arr[m]:
				m = j
		if m!=i:
			arr[i],arr[m] = arr[m],arr[i]
	return arr

def input_array(len):
	arr = []
	for i in range(len):
		num = int(raw_input())
		arr.append(num)
	return arr

# my function test
myarr = input_array(13)
print(selection_sort(myarr))

# system sort test
sysarr = input_array(13)
sysarr.sort()
print(sysarr)

# The password lock srceen
# 74568213
