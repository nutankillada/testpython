When you restart your **VM (Virtual Machine)**, environment variables might be lost because they are set **temporarily** in the current session. By default, they do **not persist** after a reboot unless explicitly configured.  

---

## **🔹 Why Do Environment Variables Disappear After Restart?**
1. **Temporary Shell Variables**  
   - If you set an environment variable using:
     ```bash
     export jira_email="your_email@example.com"
     export jira_api_token="your_api_token"
     ```
     - This only applies to the **current session**.
     - It **disappears** after a restart or even after closing the terminal.

2. **Non-Persistent Variables in `.bashrc`, `.zshrc`, or `.profile` Not Set**  
   - Persistent environment variables must be saved in startup files like:
     - `~/.bashrc`
     - `~/.profile`
     - `~/.bash_profile`
     - `~/.zshrc` (for Zsh users)

3. **Docker or Cloud VM Behavior**  
   - If using a **Docker container**, every restart creates a **new session** unless variables are set in the **Dockerfile** or **compose file**.
   - Some **cloud VMs (AWS, GCP, Azure)** reset non-persistent configurations when restarted.

---

## **✅ How to Make Environment Variables Persistent**
### **1. Add to `~/.bashrc` or `~/.profile` (For Linux/macOS)**
Edit your **shell profile**:
```bash
nano ~/.bashrc
```
or  
```bash
nano ~/.profile
```
Add these lines at the bottom:
```bash
export jira_email="your_email@example.com"
export jira_api_token="your_api_token"
```
Save the file (`Ctrl + X`, then `Y`, then `Enter`).

Then apply the changes:
```bash
source ~/.bashrc
```
or  
```bash
source ~/.profile
```

### **2. Add to `/etc/environment` (System-Wide)**
If you want all users to have access:
```bash
sudo nano /etc/environment
```
Add:
```
jira_email=your_email@example.com
jira_api_token=your_api_token
```
Save and reboot.

### **3. For Windows (Persistent Variables)**
Use PowerShell:
```powershell
[System.Environment]::SetEnvironmentVariable("jira_email", "your_email@example.com", "Machine")
[System.Environment]::SetEnvironmentVariable("jira_api_token", "your_api_token", "Machine")
```
Or manually:
1. **Search** for "Environment Variables" in Windows.
2. Click "Edit the system environment variables."
3. Click "Environment Variables."
4. Under "System Variables," click "New" and add `jira_email` and `jira_api_token`.
5. Click **OK** and restart your system.

---

## **💡 Verify Environment Variables After Restart**
To check if variables persist after reboot:
```bash
echo $jira_email
echo $jira_api_token
```
If they are empty, the persistence settings need to be fixed.

---

### **🚀 Summary**
- **Temporary variables** disappear after a reboot.
- To make them **permanent**, add them to `~/.bashrc`, `~/.profile`, or `/etc/environment`.
- For **Windows**, set them via **System Environment Variables**.




The difference between adding environment variables in **`~/.bashrc`** and **`~/.profile`** mainly depends on **when** and **how** they are loaded.  

---

## **🔹 `~/.bashrc` vs `~/.profile`: Key Differences**  

| Feature         | `~/.bashrc` | `~/.profile` |
|---------------|------------|-------------|
| **When It Runs** | Every time a **new terminal** (interactive shell) starts | Only when a **user logs in** (login shell) |
| **Shell Type** | Runs in **interactive, non-login shells** (like opening a new terminal window) | Runs in **login shells** (like SSH or first terminal session) |
| **Persistence** | Only applies to interactive terminals | Applies to all login-based sessions |
| **Best for** | Aliases, custom prompts, interactive commands | Persistent environment variables and system-wide settings |

---

## **🔹 When to Use `~/.bashrc`**
Use **`~/.bashrc`** when you want settings to be applied **only when opening a new terminal session** (interactive shell).  
Example:
```bash
export PATH=$PATH:/usr/local/bin/customscript
alias ll='ls -la'
```
- This applies only to **new terminal sessions**, not to scripts running in non-interactive modes.  
- It is ideal for **command shortcuts, aliases, or interactive tools**.  

---

## **🔹 When to Use `~/.profile`**
Use **`~/.profile`** when you want **environment variables** to be **set system-wide** after user login (affecting all processes).  
Example:
```bash
export jira_email="your_email@example.com"
export jira_api_token="your_api_token"
```
- This applies to **all login sessions**, including **SSH connections and background processes**.  
- It ensures that **environment variables persist across sessions**.

---

## **🔹 Why Does It Matter?**
- If you add a variable in **`~/.bashrc`**, it may **not be available** in scripts or SSH logins.  
- If you add it in **`~/.profile`**, it ensures the variable is loaded at **every login**, even for non-interactive processes.

---

## **✅ Best Practice**
- **For environment variables** (like API keys, credentials) → Use `~/.profile`.  
- **For aliases and terminal settings** (like `alias ll='ls -la'`) → Use `~/.bashrc`.  
- **If unsure**, add it to both:  
  ```bash
  echo 'export jira_email="your_email@example.com"' >> ~/.profile
  echo 'export jira_email="your_email@example.com"' >> ~/.bashrc
  source ~/.profile
  ```





even after adding it in both ~/.bashrc and ~/.profile, env var not added and not showing after running env:
export jira_email="your_email@example.com"
export jira_api_token="your_api_token"



If the environment variables are not being applied even after adding them to both `~/.bashrc` and `~/.profile`, there are a few common reasons for this. Let's troubleshoot step-by-step:

---

### **1. Check if You Have Saved and Sourced the Files**    [It WORKED]
- **Make sure you saved** the changes to `~/.bashrc` and `~/.profile` after editing them.
  
For example, after editing the files, run the following to **apply changes**:

```bash
source ~/.bashrc
source ~/.profile
```

This reloads the configuration files and applies the changes in the current shell.

### **2. Check the Shell You Are Using**
- Make sure you're using **Bash** and not a different shell (like Zsh or Fish). For example, if you're using **Zsh**, you would need to add the variables to **`~/.zshrc`**.

To check your shell:
```bash
echo $SHELL
```
If you're using **Zsh**, you should add the environment variables to `~/.zshrc` instead of `~/.bashrc` or `~/.profile`.

---

### **3. Ensure It's a Login Shell**
- **`~/.profile`** is only sourced for **login shells**. If you are opening a new terminal window, it may not be considered a login shell. For example, terminals opened through GUI applications often don't invoke login shells.

To force a login shell (if you're using Bash), you can do this:
```bash
bash --login
```

This forces Bash to act as a **login shell**, which will read the `~/.profile` file.

---

### **4. Check for Syntax Errors**
- A **syntax error** in `~/.bashrc` or `~/.profile` can cause the file not to be loaded correctly. Double-check the syntax.

For example, make sure there are **no extra spaces** or missing quotes:
```bash
export jira_email="your_email@example.com"
export jira_api_token="your_api_token"
```

### **5. Verify the Variables Are in the Correct Location**
- Ensure you added the `export` lines **at the end** of the files (`~/.bashrc` or `~/.profile`), so no other commands are overriding them.

---

### **6. Check for Overriding Files**
- Sometimes other files or configurations (like `.bash_profile`, `.bash_login`, or system-wide `/etc/profile`) can override these settings. To check for overrides, search for references to `jira_email` and `jira_api_token` in the following files:

```bash
grep -r "jira_email" ~
```

This will search for `jira_email` in your home directory and show you if it's being set or overwritten anywhere else.

---

### **7. Add Variables to `/etc/environment` (System-Wide)**
If all else fails and you want the environment variables to be set **system-wide** (for all users), you can add them to the `/etc/environment` file.

1. Open the file:
   ```bash
   sudo nano /etc/environment
   ```

2. Add the variables:
   ```bash
   jira_email="your_email@example.com"
   jira_api_token="your_api_token"
   ```

3. Save and reboot the system.

---

### **8. Verify After Restart**
After making sure you have saved everything and sourced the appropriate files, run:
```bash
env | grep jira_
```
This should show your environment variables if they are set correctly. If they're still not showing, try rebooting your VM or checking for potential errors in your shell configuration files.

---

### **Summary Checklist**
- **Source** the files: `source ~/.bashrc` and `source ~/.profile`
- **Check your shell**: Ensure you're using Bash and not another shell like Zsh.
- **Ensure you're using a login shell** if using `~/.profile`.
- **Check for syntax errors** in the files.
- **Search for overrides** in other configuration files like `.bash_profile`.

Let me know if you need help with any specific step! 😊