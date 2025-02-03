class BufferUtiles:

    @staticmethod
    def calc_ret_buffer_id(buffer_length, current_id) -> None:
        if current_id < buffer_length:
            if current_id - 1 > 0:
                return current_id - 1
            else:
                return None
