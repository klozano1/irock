
CREATE TABLE DEPT(
	DEPTNO			INT(2),
	DNAME			VARCHAR(14),
	LOC			VARCHAR(13),
	CONSTRAINT DEPT_DEPTNO_PK PRIMARY KEY(DEPTNO));

INSERT INTO DEPT VALUES(10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES(20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES(30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES(40,'OPERATIONS','BOSTON');

create table emp
(	EMPNO				INT(4),
	ENAME				VARCHAR(10),
	JOB				VARCHAR(9),
	MGR				INT(4),
	HIREDATE			DATE,
	SAL	                       	DEC(7,2),
	COMM 	                      	DEC(7,2),
	DEPTNO				INT(2) ,
	CONSTRAINT EMP_EMPNO_PK PRIMARY KEY(EMPNO),
        CONSTRAINT EMP_DEPTNO_FK FOREIGN KEY(DEPTNO)
	REFERENCES DEPT(DEPTNO));

INSERT INTO EMP VALUES(7369,'SMITH','CLERK',7902,'1980-12-17',800.00,NULL,20);
INSERT INTO EMP VALUES(7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600.00,300.00,30);
INSERT INTO EMP VALUES(7521,'WARD','SALESMAN',7698,'1981-02-22',1250.00,500.00,30);
INSERT INTO EMP VALUES(7566,'JONES','MANAGER',7839,'1981-04-02',2975.00,NULL,20);
INSERT INTO EMP VALUES(7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250.00,1400.00,30);
INSERT INTO EMP VALUES(7698,'BLAKE','MANAGER',7839,'1981-05-31',2850.00,NULL,30);
INSERT INTO EMP VALUES(7782,'CLARK','MANAGER',7839,'1981-06-09',2450.00,NULL,10);
INSERT INTO EMP VALUES(7788,'SCOTT','ANALYST',7566,'1981-06-09',3000.00,NULL,20);
INSERT INTO EMP VALUES(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000.00,NULL,10);
INSERT INTO EMP VALUES(7844,'TURNER','SALESMAN',7698,'1981-11-02',1500.00,0.00,30);
INSERT INTO EMP VALUES(7876,'ADAMS','CLERK',7788,'1981-06-12',1100.00,NULL,20);
INSERT INTO EMP VALUES(7900,'JAMES','CLERK',7698,'1981-12-01',950.00,NULL,30);
INSERT INTO EMP VALUES(7902,'FORD','ANALYST',7566,'1981-12-03',3000.00,NULL,20);
INSERT INTO EMP VALUES(7934,'MILLER','CLERK',7782,'1981-06-23',1300.00,NULL,10);