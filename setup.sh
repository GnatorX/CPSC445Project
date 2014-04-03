#!/usr/bin/expect -f


log_user 1;
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
send -- "GGCGGCGCCGGCCGGCGGCCCACGGCCCCCCAGCCAGGGGGGCUGAGGAAACUCCGCCCUCCCCGCGGCGGCCGGGCCCCGCAAGGGGCACGGGUGAAACCCGUGGCAACGGCACAGAAACGACACGGCCCCGGGGCGUGUCGAGGACGCGGCUAGGCCGCCCUGGCAACAGGGCGGCAGCAAACCGCAGAGGAACCCCGGGGAUGCGGUGAAACGGCCGCCCCCGGCGGAGCAAGGCCCCCGGGCGGUGAGGGCCGCGCGAAGCCCGGGGGGAGACCGCUUAGCCCAAUGCCGCCGAAGUACAGAAGGCGGGUUAUGGCCGGCGCCGCC\r"
expect -exact "GGCGGCGCCGGCCGGCGGCCCACGGCCCCCCAGCCAGGGGGGCUGAGGAAACUCCGCCCUCCCCGCGGCGGCCGGGCCCCGCAAGGGGCACGGGUGAAACCCGUGGCAACGGCACAGAAACGACACGGCCCCGGGGCGUGUCGAGGACGCGGCUAGGCCGCCCUGGCAACAGGGCGGCAGCAAACCGCAGAGGAACCCCGGGGAUGCGGUGAAACGGCCGCCCCCGGCGGAGCAAGGCCCCCGGGCGGUGAGGGCCGCGCGAAGCCCGGGGGGAGACCGCUUAGCCCAAUGCCGCCGAAGUACAGAAGGCGGGUUAUGGCCGGCGCCGCC\r"

send -- "(((((((((((((((((((((.(((((((((.....))))))))).))..........((((........((((((((((....)))))((((((...))))))((...((((.(.(....(.(.(((((((((((..(.((......((((.(.((((((((((....)))))))))..).).)))).)).)..)))))))).).))))....)))))).))))))))))).(.(((((((((((..((.(.....).))..)))))))))....))..).........)))))).....................)))))))))))))\r"
sleep 1
expect -re ".*"
puts $expect_out(buffer);




