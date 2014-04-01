#!/usr/bin/expect -f



set timeout -1
spawn $env(SHELL)
match_max 100000

send -- "RNAeval -v -d2\r"
expect -exact "RNAeval -v -d2\r
\r
Input sequence & structure;   @ to quit\r
Use '&' to connect 2 sequences that shall form a complex.\r
....,....1....,....2....,....3....,....4....,....5....,....6....,....7....,....8\r
"
send -- "GGCGGCGCCGGCCGGCGGCCCACGGCCCCCCAGCCAGGGGGGCUGAGGAAACUCCGCCCUCCCCGCGGCGGCCGGGCCCCGCAAGGGGCACGGGUGAAACCCGUGGCAACGGCACAGAAACGACACGGCCCCGGGGCGUGUCGAGGACGCGGCUAGGCCGCCCUGGCAACAGGGCGGCAGCAAACCGCAGAGGAACCCCGGGGAUGCGGUGAAACGGCCGCCCCCGGCGGAGCAAGGCCCCCGGGCGGUGAGGGCCGCGCGAAGCCCGGGGGGAGACCGCUUAGCCCAAUGCCGCCGAAGUACAGAAGGCGGGUUAUGGCCGGCGCCGCC"
expect -exact "GGCGGCGCCGGCCGGCGGCCCACGGCCCCCCAGCCAGGGGGGCUGAGGAAACUCCGCCCUCCCCGCGGCGGCCGGGCCCCGCAAGGGGCACGGGUGAAACCCGUGGCAACGGCACAGAAACGACACGGCCCCGGGGCGUGUCGAGGACGCGGCUAGGCCGCCCUGGCAACAGGGCGGCAGCAAACCGCAGAGGAACCCCGGGGAUGCGGUGAAACGGCCGCCCCCGGCGGAGCAAGGCCCCCGGGCGGUGAGGGCCGCGCGAAGCCCGGGGGGAGACCGCUUAGCCCAAUGCCGCCGAAGUACAGAAGGCGGGUUAUGGCCGGCGCCGCC"
send -- "\r"
expect -exact "\r
"
send -- "(((((((((((((((((((((.(((((((((.....))))))))).))..........((((........((((((((((....)))))((((((...))))))((...((((.(.(....(.(.(((((((((((..(.((......((((.(.((((((((((....)))))))))..).).)))).)).)..)))))))).).))))....)))))).))))))))))).(.(((((((((((..((.(.....).))..)))))))))....))..).........)))))).....................)))))))))))))"
expect -exact "(((((((((((((((((((((.(((((((((.....))))))))).))..........((((........((((((((((....)))))((((((...))))))((...((((.(.(....(.(.(((((((((((..(.((......((((.(.((((((((((....)))))))))..).).)))).)).)..)))))))).).))))....)))))).))))))))))).(.(((((((((((..((.(.....).))..)))))))))....))..).........)))))).....................)))))))))))))"
send -- "\r"
