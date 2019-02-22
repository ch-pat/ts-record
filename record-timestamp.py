from time import time
import fileinput

def timestamp_convert(ts_list):
    '''converts every element of ts_list (timestamps in seconds) in a timestamp string
       returns a list of converted timestamps'''
    result = []
    for stamp in ts_list:
        minutes = str(int(stamp // 60)).zfill(2)
        seconds = str(int((stamp % 60) // 1)).zfill(2)
        milli = str(round(stamp % 1, 3))[2:]
        timestamp = "[{}:{}.{}]".format(minutes, seconds, milli)
        result += [timestamp]
    return result

def stamp_print(ts_list):
    for ts in ts_list:
        print(ts)

def add_stamps_to_file(ts_list, file):
    index = 0
    for line in fileinput.input(file, inplace=True):
        print("{}{}".format(ts_list[index],line))
        index = min(len(ts_list)-1, index+1)


if __name__ == "__main__":
    input("Questo programma serve a generare i timestamp per file .lrc.\n Immetti Q per terminare la raccolta di timestamp in qualunque momento.\nPremi invio per avviare il timer. In seguito all'avvio, premi invio per generare un timestamp per la prossima riga della canzone.")
    start_time = time()
    timestamps = []
    counter = 1
    while True:
        if input() not in ["Q", "q"]:
            current_time_stamp = time() - start_time
            print("Timestamp #{} = {}".format(counter, current_time_stamp))
            counter += 1
            timestamps += [current_time_stamp]
        else:
            print("Raccolta terminata")
            break
    # Inputs done, convert
    converted = timestamp_convert(timestamps)
    print("Conversione terminata")
    print("Timestamp formattati:\n")
    stamp_print(converted)
    print("\nSe non si desidera fornire un file testo da modificare, copiare i timestamp adesso.\n")
    file = input("Se si desidera fornire un file, immettere ora il nome del file (ricordare di aggiungere l'estensione, es: ciao.txt) presente nella cartella attuale o immettere Q per uscire\n")
    if file not in ["q", "Q"]:
        try:
            add_stamps_to_file(converted, file)
            print("\nInserimento Timestamps completato con successo!")
            input()
        except:
            print("ERRORE: Il file inserito non è corretto o è inesistente")
