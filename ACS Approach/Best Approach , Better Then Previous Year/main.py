import pa
import pada
import time

   
pa.start_process_of_PA()
details = pa.find_distance()

time.sleep(20)

pada.start_process_of_PADA(details,'RED')
