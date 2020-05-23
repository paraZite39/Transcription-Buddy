import re

def bracket_timestamps(file):
    '''
    In - File name (ex. transcript.txt)
    Out - None, but creates an outfile (ex. transcriptout.txt) with bracketed timestamps
    
    Surrounds all timestamps with square brackets (ex. [1:00:15]).
    Useful for my own transcription projects that use oTranscript's automatic timestamps.
    Works for a maximum of 99 hours (99:59:59).
    '''
    
    file_name = file.split(".")[0]      # extracting file name (ex. file.txt -> file)
    in_transcr = open(file)
    out_transcr = open("{}out.txt".format(file_name), "w")
    
    timestampRegex = re.compile(r" (((\d)?\d:)?\d\d:\d\d) ")     # pattern of timestamps (dd:dd or d:dd:dd)
    
    for line in in_transcr.readlines():
        finline = line
        matches = timestampRegex.findall(line)      # find all timestamps, put 'em in a list
        for match in matches:
            finline = re.sub(match[0], "[{}]".format(match[0]), finline)    # replace timestamp with [timestamp]
    
        out_transcr.write(finline)      # write formatted line to outfile
            
    in_transcr.close()
    out_transcr.close()
