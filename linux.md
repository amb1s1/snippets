# Nmap 

### Scan for different UDP open ports
`nmap -s U 10.55.10.151 -p 135,53248,389,49152-65535,3268,445,53,88,123,5722`

### Scan for different TCP open ports  
`nmap -s T 10.55.10.151 -p 135,53248,389,49152-65535,3268,445,53,88,123,5722`

### Full Scan - By default NMAP scan for TCP ports
`nmap 10.55.10.151`

### Ping scan for that subnet - Will give a list of Active Host
`nmap -sP 10.5.90.0/24`

### Creates a report with all active host with OS/Ports information
`nmap -O -oG report.txt 192.168.1.0/24`

---
## Ouput example:
```
PORT   STATE SERVICE
80/tcp open  http
```

## Output meaning
    - State open, the application is running
	- State close, the application is not running
	- State filter, port is blocked

> @Ur_Average_Neteng
