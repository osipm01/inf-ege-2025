from  Buffer import Buffer_R2

buffer = Buffer_R2([1, 2])

buffer.create_buffer2r()


print(buffer.get_value_from_buffer())
buffer.set_next_value_to_buffer(5)
print(buffer.get_value_from_buffer())
buffer.set_next_value_to_buffer(9)
print(buffer.get_value_from_buffer())
print(buffer.get_value_from_buffer())


