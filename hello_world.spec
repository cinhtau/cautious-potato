Summary: Outputs "hello world" on execution.
Name: hello_world
Version: 1.0.0
Release: 1
License: GPLv3+

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%pre
 echo "this is the pre-install sh command"
 mkdir -p /opt/hello_world/

%post
 echo "this is the post-install sh command"

%files

%defattr(750,tan,tan)
 /opt/hello_world/hello_world

%preun
 echo "the pre-uninstall sh commands"

%postun
 echo "the post-uninstall sh commands"