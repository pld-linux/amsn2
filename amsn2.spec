Summary:	MSN Messenger clone for Linux
Summary(de.UTF-8):	MSN Messenger-Klon für Linux
Summary(fr.UTF-8):	Clône MSN Messenger pour Linux
Summary(pl.UTF-8):	Klon MSN Messengera dla Linuksa
Name:		amsn2
Version:	0.97.2
Release:	0.12
Epoch:		0
License:	GPL
Group:		Applications/Communications
Source0:	%{name}.tar.bz2
# Source0-md5:	19c94e6676b42a6a9a47948334864b34
URL:		http://www.amsn-project.net/forums/viewtopic.php?t=5299
Requires:	python-papyon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Tcl/Tk clone that implements the Microsoft Messenger (MSN) for
Unix, Windows, or Macintosh platforms. It supports file transfers,
groups, and many more features.

%description -l de.UTF-8
amsn ist ein Microsoft Messenger (MSN) Client für UNIX, Windows und
Macintosh, der in Tcl/Tk geschrieben ist. Es unterstützt
Dateiübertragungen, Gruppen uvm.

%description -l fr.UTF-8
amsn est un client Microsoft Messenger (MSN) pour UNIX, Windows et
Macintosh écrit en Tcl/Tk. Il supporte les tranferts de fichiers, les
groupes et beaucoup d'autres possibilités.

%description -l pl.UTF-8
amsn to klient Microsoft Messengera (MSN) dla Uniksów, Windows i
Macintosha napisany w Tcl/Tk. Obsługuje przesyłanie plików, grupy i
wiele więcej możliwości.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
