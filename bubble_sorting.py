def bubble_sort(arr):
	n=len(arr)
	if n<=1:
		return 
	for i in range(n-1):
		swaped=False#设置标志位 False表示还是无序的
		for j in range(n-i-1):
			if arr[j]<arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
				swaped=True
		if not swaped:
			break
			#如果上面的内层for循环没有做出交换操作 那么说明arr已经是有序的
					

