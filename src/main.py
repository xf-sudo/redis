from classmodul.redis import Redis
from queue import Queue
import traceback

def process_queue(q, redis_store):
    """
    Execute commands Queue
    :param q: command queue to be processed
    :param redis_store: object store to be changed
    """
    #dequeue all the commands and process them
    while not q.empty():
        fields_of_req_2_process = q.get()
        #get redis function by name
        redis_func = getattr(redis_store, fields_of_req_2_process[0].lower())
        try:
            #execute redis function
            result = redis_func(*fields_of_req_2_process[1:])
            if result is not None:
                print(result)
        except:
            print(traceback.format_exc())

def redis_cli_console():
    """
    Simple redis console
    """
    #object to store and process information about the key values pairs
    redis_store = Redis()
    #queue to receive the redis requests
    q = Queue()
    #boolean variable to know if it is in transaction mode.
    transaction = False

    while True:

        text_command = input('Command{}: '.format('{TX}' if transaction else ''))
        command_fields = text_command.split()

        if (len(command_fields) != 0 and
                command_fields[0].upper() in (
                                            Redis.basic_commands
                                            + Redis.transactional_commands)):
            if command_fields[0].lower() == 'begin':
                #begin a transaction
                transaction = True
                continue
            elif command_fields[0].lower() == 'end':
                #exits the program
                break
            elif command_fields[0].lower() == 'rollback':
                if transaction:
                    #delete all enqueued commands to be processed
                    q.queue.clear()
                    transaction = False
                else:
                    #not in transaction mode so there is no rollback to be done.
                    print('NO TRANSACTION')
                continue
            elif command_fields[0].lower() == 'commit':
                if transaction:
                    #closes the transaction mode
                    transaction = False
                else:
                    #not in transaction mode so there is no commit to be done.
                    print('NO TRANSACTION')
            else:
                #enqueue the command
                q.put(command_fields)

            #if not in transaction mode do not process the queue
            if transaction:
                continue
        else:
            #Unknow command prints an error message
            print('Error')

        #process the command queue
        process_queue(q, redis_store)

if __name__ == '__main__':
    redis_cli_console()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
