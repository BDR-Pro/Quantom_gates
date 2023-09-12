OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[1];
reset q[0];
reset q[1];
reset q[2];
barrier q[1];
barrier q[2];
x q[0];
barrier q[0];
cx q[1], q[2];
cx q[0], q[2];
measure q[2] -> c[0];
