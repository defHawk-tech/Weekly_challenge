# Cyber Riddle Solution: Buffer Overflow Challenge

Welcome to the solution for the **Cyber Riddle Challenge** presented by DefHawk! This challenge involves analyzing a simple C program and uncovering the vulnerability hidden within. Below, we will walk through the solution and explain the root cause of the issue.

---

## Challenge Code

```c
int main(int argc, char *argv[]) {
    char buffer[10];
    if (argc < 2) {
        exit(0);
    }
    strcpy(buffer, argv[1]);
    return 0;
}
```

---

## Riddle Hint

> _"I am the whisper that slips past boundaries, With every step, I push too far. I am uninvited, overwriting what's near!"_

This hint refers to a **buffer overflow** vulnerability, where data exceeds the allocated memory boundary and overwrites adjacent memory.

---

## Vulnerability Analysis

### Key Issues:
1. **Use of `strcpy` without Bounds Checking**:
   - The `strcpy` function copies data from `argv[1]` into the `buffer` array without verifying the size of the input.
   - The `buffer` is only 10 bytes long, so any input larger than 10 bytes will overflow the buffer and overwrite adjacent memory.

2. **No Input Validation**:
   - The program assumes that `argv[1]` will fit into the buffer without performing any size checks.

### Exploitation:
- An attacker can exploit this by providing a long input string as an argument to the program, causing memory corruption.
- Depending on the environment, this may lead to:
  - Crashing the program.
  - Overwriting the return address, enabling code execution (e.g., shellcode injection).

---

## Demonstration

### Exploit Example
To trigger the vulnerability, compile and execute the program:

```bash
gcc -o challenge challenge.c
./challenge AAAAAAAAAAAAAAAAAA
```

In this example, providing a string longer than 10 characters (e.g., `AAAAAAAAAAA`) will overflow the buffer and potentially crash the program.

---

## Mitigation Strategies

1. **Bounds Checking**:
   Replace `strcpy` with safer alternatives like `strncpy`:
   ```c
   strncpy(buffer, argv[1], sizeof(buffer) - 1);
   buffer[sizeof(buffer) - 1] = '\0'; // Ensure null-termination
   ```

2. **Input Validation**:
   Validate the length of the input before copying it:
   ```c
   if (strlen(argv[1]) >= sizeof(buffer)) {
       printf("Input too long!\n");
       exit(1);
   }
   strcpy(buffer, argv[1]);
   ```

3. **Compiler Protections**:
   Enable compiler-level protections such as stack canaries and ASLR:
   ```bash
   gcc -o challenge -fstack-protector -D_FORTIFY_SOURCE=2 challenge.c
   ```

---

## Conclusion

This challenge highlights the dangers of improper memory handling in C programs. Understanding and mitigating buffer overflow vulnerabilities is critical for secure software development.

If you found this helpful, don't forget to share your feedback and explore more challenges! 

---

### Resources
- [Buffer Overflow Explained](https://owasp.org/www-community/attacks/Buffer_Overflow)
- [Secure Coding Practices](https://cwe.mitre.org/top25/)
- [Introduction to Exploitation](https://www.exploit-db.com/)
