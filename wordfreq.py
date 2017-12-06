most_common_english_words = [ "the","be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at"]
color_esc_seqs = {"default":"0", "black":"30", "red":"31", "green":"32", "yellow":"33", "blue":"34", "magenta":"35", "cyan":"36", "white":"37"}

def canonicalize_word(word):
    trimed_string = word.strip()
    return trimed_string.lower()

def set_color(word, color):
    return "\x1b[1;" + color_esc_seqs[color] + "m" + word + "\x1b[0m"

def format_line(line, common_words=[]):
    return ' '.join([set_color(w,'green') if (canonicalize_word(w) in common_words) else w for w in line.split()])

print format_line("To be or not to be, that is the question")
print format_line("To be or not to be, that is the question", most_common_english_words)
