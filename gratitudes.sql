--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.1
-- Dumped by pg_dump version 9.6.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: comments; Type: TABLE; Schema: public; Owner: jacqui
--

CREATE TABLE comments (
    comment_id integer NOT NULL,
    text text NOT NULL,
    gratitude_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE comments OWNER TO jacqui;

--
-- Name: comments_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: jacqui
--

CREATE SEQUENCE comments_comment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE comments_comment_id_seq OWNER TO jacqui;

--
-- Name: comments_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jacqui
--

ALTER SEQUENCE comments_comment_id_seq OWNED BY comments.comment_id;


--
-- Name: entries; Type: TABLE; Schema: public; Owner: jacqui
--

CREATE TABLE entries (
    entry_id integer NOT NULL,
    date_posted timestamp without time zone NOT NULL,
    date_updated timestamp without time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE entries OWNER TO jacqui;

--
-- Name: entries_entry_id_seq; Type: SEQUENCE; Schema: public; Owner: jacqui
--

CREATE SEQUENCE entries_entry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE entries_entry_id_seq OWNER TO jacqui;

--
-- Name: entries_entry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jacqui
--

ALTER SEQUENCE entries_entry_id_seq OWNED BY entries.entry_id;


--
-- Name: gratitudes; Type: TABLE; Schema: public; Owner: jacqui
--

CREATE TABLE gratitudes (
    gratitude_id integer NOT NULL,
    text text NOT NULL,
    entry_id integer NOT NULL
);


ALTER TABLE gratitudes OWNER TO jacqui;

--
-- Name: gratitudes_gratitude_id_seq; Type: SEQUENCE; Schema: public; Owner: jacqui
--

CREATE SEQUENCE gratitudes_gratitude_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE gratitudes_gratitude_id_seq OWNER TO jacqui;

--
-- Name: gratitudes_gratitude_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jacqui
--

ALTER SEQUENCE gratitudes_gratitude_id_seq OWNED BY gratitudes.gratitude_id;


--
-- Name: tags; Type: TABLE; Schema: public; Owner: jacqui
--

CREATE TABLE tags (
    tag_id integer NOT NULL,
    gratitude_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE tags OWNER TO jacqui;

--
-- Name: tags_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: jacqui
--

CREATE SEQUENCE tags_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tags_tag_id_seq OWNER TO jacqui;

--
-- Name: tags_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jacqui
--

ALTER SEQUENCE tags_tag_id_seq OWNED BY tags.tag_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: jacqui
--

CREATE TABLE users (
    user_id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    last_name character varying(64) NOT NULL,
    username character varying(64) NOT NULL,
    email character varying(64) NOT NULL,
    password character varying(64) NOT NULL,
    location character varying(64),
    profile_image text,
    date_joined timestamp without time zone NOT NULL
);


ALTER TABLE users OWNER TO jacqui;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: jacqui
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_user_id_seq OWNER TO jacqui;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jacqui
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: comments comment_id; Type: DEFAULT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY comments ALTER COLUMN comment_id SET DEFAULT nextval('comments_comment_id_seq'::regclass);


--
-- Name: entries entry_id; Type: DEFAULT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY entries ALTER COLUMN entry_id SET DEFAULT nextval('entries_entry_id_seq'::regclass);


--
-- Name: gratitudes gratitude_id; Type: DEFAULT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY gratitudes ALTER COLUMN gratitude_id SET DEFAULT nextval('gratitudes_gratitude_id_seq'::regclass);


--
-- Name: tags tag_id; Type: DEFAULT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY tags ALTER COLUMN tag_id SET DEFAULT nextval('tags_tag_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: jacqui
--

COPY comments (comment_id, text, gratitude_id, user_id) FROM stdin;
\.


--
-- Name: comments_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jacqui
--

SELECT pg_catalog.setval('comments_comment_id_seq', 1, false);


--
-- Data for Name: entries; Type: TABLE DATA; Schema: public; Owner: jacqui
--

COPY entries (entry_id, date_posted, date_updated, user_id) FROM stdin;
1	2015-12-12 00:00:00	2015-12-12 00:00:00	1
2	2015-12-21 00:00:00	2015-12-21 00:00:00	2
\.


--
-- Name: entries_entry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jacqui
--

SELECT pg_catalog.setval('entries_entry_id_seq', 2, true);


--
-- Data for Name: gratitudes; Type: TABLE DATA; Schema: public; Owner: jacqui
--

COPY gratitudes (gratitude_id, text, entry_id) FROM stdin;
1	Setting up the xmas tree w/lights, the house smelling of pine, listening to Arcade Fire w/Geoff and Mike.	1
2	Awesome Bailee xmas party!	1
3	That I get to work next to Kristin on this website build, she rocks :)	1
4	The huge stack of crossword puzzles that mom's saved for me from the Projo.	2
5	Grandma getting so happy and excited to hear me play the piano.	2
6	Getting to sleep in the living room with my own christmas tree.	2
\.


--
-- Name: gratitudes_gratitude_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jacqui
--

SELECT pg_catalog.setval('gratitudes_gratitude_id_seq', 6, true);


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: jacqui
--

COPY tags (tag_id, gratitude_id, user_id) FROM stdin;
\.


--
-- Name: tags_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jacqui
--

SELECT pg_catalog.setval('tags_tag_id_seq', 1, false);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: jacqui
--

COPY users (user_id, first_name, last_name, username, email, password, location, profile_image, date_joined) FROM stdin;
1	Jacqui	Watts	jacquelope	jacquelineawatts@gmail.com	tester	San Francisco	https://scontent-sjc2-1.xx.fbcdn.net/v/t1.0-1/p320x320/12928314_10103831599186320_7570467518951458496_n.jpg?oh=809c84d892fe71b3a0a721162f1cb309&oe=58A9E89E	2017-02-20 00:00:00
2	Michaela	D'Amico	kaylala	michaeladamico@gmail.com	testing	Tena, Ecuador	https://scontent-sjc2-1.xx.fbcdn.net/v/t1.0-1/p320x320/10590394_10102505355658989_740112908400003827_n.jpg?oh=bec858284ab0f8f888b79a8aa0d0c70e&oe=58AB7845	2017-02-20 00:00:00
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jacqui
--

SELECT pg_catalog.setval('users_user_id_seq', 2, true);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (comment_id);


--
-- Name: entries entries_pkey; Type: CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY entries
    ADD CONSTRAINT entries_pkey PRIMARY KEY (entry_id);


--
-- Name: gratitudes gratitudes_pkey; Type: CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY gratitudes
    ADD CONSTRAINT gratitudes_pkey PRIMARY KEY (gratitude_id);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (tag_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: comments comments_gratitude_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_gratitude_id_fkey FOREIGN KEY (gratitude_id) REFERENCES gratitudes(gratitude_id);


--
-- Name: comments comments_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: entries entries_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY entries
    ADD CONSTRAINT entries_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: gratitudes gratitudes_entry_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY gratitudes
    ADD CONSTRAINT gratitudes_entry_id_fkey FOREIGN KEY (entry_id) REFERENCES entries(entry_id);


--
-- Name: tags tags_gratitude_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY tags
    ADD CONSTRAINT tags_gratitude_id_fkey FOREIGN KEY (gratitude_id) REFERENCES gratitudes(gratitude_id);


--
-- Name: tags tags_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: jacqui
--

ALTER TABLE ONLY tags
    ADD CONSTRAINT tags_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- PostgreSQL database dump complete
--

