USE [master]
GO
/****** Object:  Database [littleking]    Script Date: 18/12/2020 9:04:29 am ******/
CREATE DATABASE [littleking]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'littleking', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\littleking.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'littleking_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\littleking_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [littleking] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [littleking].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [littleking] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [littleking] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [littleking] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [littleking] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [littleking] SET ARITHABORT OFF 
GO
ALTER DATABASE [littleking] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [littleking] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [littleking] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [littleking] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [littleking] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [littleking] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [littleking] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [littleking] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [littleking] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [littleking] SET  ENABLE_BROKER 
GO
ALTER DATABASE [littleking] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [littleking] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [littleking] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [littleking] SET ALLOW_SNAPSHOT_ISOLATION ON 
GO
ALTER DATABASE [littleking] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [littleking] SET READ_COMMITTED_SNAPSHOT ON 
GO
ALTER DATABASE [littleking] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [littleking] SET RECOVERY FULL 
GO
ALTER DATABASE [littleking] SET  MULTI_USER 
GO
ALTER DATABASE [littleking] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [littleking] SET DB_CHAINING OFF 
GO
ALTER DATABASE [littleking] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [littleking] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [littleking] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'littleking', N'ON'
GO
ALTER DATABASE [littleking] SET QUERY_STORE = ON
GO
ALTER DATABASE [littleking] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 7), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 10, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [littleking]
GO
/****** Object:  UserDefinedFunction [dbo].[NoOfBags_Balance]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create function [dbo].[NoOfBags_Balance] (@FarmerID int)
returns INT
as
begin
    return
	(select isnull(sum(NoOfBags),0)-(select isnull(sum(NoOfBags),0) from v_Transaction where TransactionType = 'checkout' and FarmerID = @FarmerID)
from v_Transaction where TransactionType = 'checkin' and FarmerID = @FarmerID )
end  
GO
/****** Object:  Table [dbo].[Farmer]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Farmer](
	[FarmerID] [int] IDENTITY(1,1) NOT NULL,
	[FirstName] [varchar](225) NOT NULL,
	[LastName] [varchar](225) NOT NULL,
	[Village] [varchar](225) NOT NULL,
	[Mandal] [varchar](225) NOT NULL,
	[PANNumber] [char](25) NULL,
	[EffFromDate] [datetime] NOT NULL,
	[EffThruDate] [datetime] NOT NULL,
	[Phone] [bigint] NOT NULL,
	[Aadhar] [bigint] NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[FarmerID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Item]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Item](
	[ItemID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](100) NOT NULL,
	[Description] [nvarchar](4000) NULL,
	[Code] [nchar](10) NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Item_ItemID] PRIMARY KEY CLUSTERED 
(
	[ItemID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RecordStatus]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RecordStatus](
	[RecordStatusID] [int] IDENTITY(1,1) NOT NULL,
	[Code] [nchar](10) NOT NULL,
	[Name] [nchar](10) NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_RecordStatus] PRIMARY KEY CLUSTERED 
(
	[RecordStatusID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Transaction]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Transaction](
	[TransactionID] [int] IDENTITY(1,1) NOT NULL,
	[ParentTransactionID] [int] NULL,
	[TransactionTypeID] [int] NOT NULL,
	[FarmerID] [int] NOT NULL,
	[Description] [nvarchar](4000) NULL,
	[ItemID] [int] NOT NULL,
	[VarietyID] [int] NOT NULL,
	[NoOfBags] [int] NOT NULL,
	[KanaBlockMapID] [int] NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Transaction] PRIMARY KEY CLUSTERED 
(
	[TransactionID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TransactionType]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TransactionType](
	[TransactionTypeID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_TransactionType] PRIMARY KEY CLUSTERED 
(
	[TransactionTypeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Variety]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Variety](
	[VarietyID] [int] IDENTITY(1,1) NOT NULL,
	[ItemID] [int] NOT NULL,
	[Name] [nvarchar](100) NOT NULL,
	[Description] [nvarchar](4000) NULL,
	[Code] [nchar](10) NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Variety_VarietyID] PRIMARY KEY CLUSTERED 
(
	[VarietyID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Block]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Block](
	[BlockID] [int] IDENTITY(1,1) NOT NULL,
	[Code] [char](10) NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Block] PRIMARY KEY CLUSTERED 
(
	[BlockID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Floor]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Floor](
	[FloorID] [int] IDENTITY(1,1) NOT NULL,
	[Code] [int] NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Floor_KEY] PRIMARY KEY CLUSTERED 
(
	[FloorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Kana]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Kana](
	[KanaID] [int] IDENTITY(1,1) NOT NULL,
	[FloorID] [int] NOT NULL,
	[KanaCode] [int] NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Kana] PRIMARY KEY CLUSTERED 
(
	[KanaID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KanaBlockMap]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KanaBlockMap](
	[KanaBlockMapID] [int] IDENTITY(1,1) NOT NULL,
	[KanaID] [int] NOT NULL,
	[BlockID] [int] NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Kana_BLOCK_MAP] PRIMARY KEY CLUSTERED 
(
	[KanaBlockMapID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[v_FloorKanaBlock]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[v_FloorKanaBlock] as
SELECT KBM.KanaBlockMapID,K.KanaID,K.KanaCode,B.BlockID,B.Code BlockCode,F.FloorID,F.Code FloorCode, LTRIM(K.KanaCode) + '('+TRIM(B.Code)+')' AS KanaBlockKey,KBM.RecordStatusID,R.Name from KanaBlockMap KBM
join Kana K ON K.KanaID = KBM.KanaID
JOIN [Block] B ON B.BlockID = KBM.BlockID
JOIN [Floor] F ON F.FloorID = K.FloorID 
JOIN RecordStatus R ON R.RecordStatusID = KBM.RecordStatusID
GO
/****** Object:  View [dbo].[v_Transaction]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[v_Transaction] AS 
SELECT	
	F.FirstName+' '+F.LastName Farmer
	,F.FarmerID
	,F.Village
	,F.Phone
	,T.NoOfBags
	,T.TransactionID
	,T.Description
	,TT.TransactionTypeID
	,TT.Name AS TransactionType
	,I.ItemID
	,I.Name AS Item
	,V.VarietyID
	,V.Name AS Variety 
	,E.KanaBlockKey
	,R.Name AS TransactionStatus
	,T.CreatedDate as TransactionDate
FROM [Transaction] T
JOIN Farmer F ON T.FarmerID = F.FarmerID
JOIN Item I ON I.ItemID = T.ItemID
JOIN Variety V ON V.VarietyID = T.VarietyID
join v_FloorKanaBlock E ON T.KanaBlockMapID = E.KanaBlockMapID
JOIN RecordStatus R ON R.RecordStatusID = T.RecordStatusID
JOIN TransactionType TT ON TT.TransactionTypeID = T.TransactionTypeID
GO
/****** Object:  Table [dbo].[Bank]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Bank](
	[BankID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](255) NOT NULL,
	[Address] [varchar](4000) NULL,
	[Phone] [varchar](10) NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Floor] PRIMARY KEY CLUSTERED 
(
	[BankID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Loan]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Loan](
	[LoanID] [int] IDENTITY(1,1) NOT NULL,
	[TransactionID] [int] NOT NULL,
	[FarmerID] [int] NOT NULL,
	[BankID] [int] NOT NULL,
	[BondNumber] [int] NOT NULL,
	[NetWeight] [int] NOT NULL,
	[ApprxCost] [float] NOT NULL,
	[AmountEligible] [float] NOT NULL,
	[AmountSanctioned] [float] NOT NULL,
	[RequestDate] [datetime] NOT NULL,
	[ApproveDate] [datetime] NOT NULL,
	[RecordStatusID] [int] NOT NULL,
	[CreatedDate] [datetime] NOT NULL,
	[CreatedUser] [varchar](225) NOT NULL,
 CONSTRAINT [PK_Loan] PRIMARY KEY CLUSTERED 
(
	[LoanID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Bank] ON 
GO
INSERT [dbo].[Bank] ([BankID], [Name], [Address], [Phone], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (1, N'ANDHRABANK', N'ANDHRAPREDESH, GUNTUR(D), NARASARAOPET(M),BANK STREET', N'4567234553', 1, CAST(N'2020-07-21T13:00:03.540' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Bank] OFF
GO
SET IDENTITY_INSERT [dbo].[Block] ON 
GO
INSERT [dbo].[Block] ([BlockID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (1, N'A         ', 1, CAST(N'2020-07-21T15:06:49.777' AS DateTime), N'sman')
GO
INSERT [dbo].[Block] ([BlockID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, N'B         ', 1, CAST(N'2020-07-21T15:06:49.810' AS DateTime), N'sman')
GO
INSERT [dbo].[Block] ([BlockID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (3, N'C         ', 1, CAST(N'2020-07-21T15:06:49.820' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Block] OFF
GO
SET IDENTITY_INSERT [dbo].[Farmer] ON 
GO
INSERT [dbo].[Farmer] ([FarmerID], [FirstName], [LastName], [Village], [Mandal], [PANNumber], [EffFromDate], [EffThruDate], [Phone], [Aadhar], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, N'SAMBASIVARAO', N'KORITALA', N'AMARAVATI', N'Narasaraopet', N'HUKS45AS                 ', CAST(N'2020-07-22T12:15:34.843' AS DateTime), CAST(N'9999-01-01T00:00:00.000' AS DateTime), 8099892109, 54354634663433, 1, CAST(N'2020-07-22T12:15:34.843' AS DateTime), N'sman')
GO
INSERT [dbo].[Farmer] ([FarmerID], [FirstName], [LastName], [Village], [Mandal], [PANNumber], [EffFromDate], [EffThruDate], [Phone], [Aadhar], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (3, N'RAMA', N'Karri', N'PRPalam', N'Narasaraopet', N'HLJPK9254A               ', CAST(N'2020-07-24T11:21:28.890' AS DateTime), CAST(N'9999-01-01T00:00:00.000' AS DateTime), 9879992109, 4234985518544, 1, CAST(N'2020-07-24T11:21:28.890' AS DateTime), N'sman')
GO
INSERT [dbo].[Farmer] ([FarmerID], [FirstName], [LastName], [Village], [Mandal], [PANNumber], [EffFromDate], [EffThruDate], [Phone], [Aadhar], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (4, N'SAMBASIVARAO', N'KING', N'PRPalam', N'Narasaraopet', N'HLJPK6554A               ', CAST(N'2020-07-24T14:30:49.517' AS DateTime), CAST(N'9999-01-01T00:00:00.000' AS DateTime), 9676393623, 42344445518544, 1, CAST(N'2020-07-24T14:30:49.517' AS DateTime), N'sman')
GO
INSERT [dbo].[Farmer] ([FarmerID], [FirstName], [LastName], [Village], [Mandal], [PANNumber], [EffFromDate], [EffThruDate], [Phone], [Aadhar], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (5, N'siva', N'Koritala', N'Jonnalagadda', N'Narasaraopet', N'HULPK9554A               ', CAST(N'2020-09-11T15:03:19.047' AS DateTime), CAST(N'9999-01-01T00:00:00.000' AS DateTime), 8099892208, 423541018544, 1, CAST(N'2020-09-11T15:03:19.047' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Farmer] ([FarmerID], [FirstName], [LastName], [Village], [Mandal], [PANNumber], [EffFromDate], [EffThruDate], [Phone], [Aadhar], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (6, N'Tharun', N'Koritala', N'Jonnalagadda', N'Narasaraopet', N'HULPK2254A               ', CAST(N'2020-09-11T15:04:28.473' AS DateTime), CAST(N'9999-01-01T00:00:00.000' AS DateTime), 8886017109, 426744018544, 1, CAST(N'2020-09-11T15:04:28.473' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Farmer] ([FarmerID], [FirstName], [LastName], [Village], [Mandal], [PANNumber], [EffFromDate], [EffThruDate], [Phone], [Aadhar], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (7, N'Babu', N'Koritala', N'Jonnalagadda', N'Narasaraopet', N'HULPK2774A               ', CAST(N'2020-09-11T15:05:22.557' AS DateTime), CAST(N'9999-01-01T00:00:00.000' AS DateTime), 8886018104, 426742455844, 1, CAST(N'2020-09-11T15:05:22.557' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
SET IDENTITY_INSERT [dbo].[Farmer] OFF
GO
SET IDENTITY_INSERT [dbo].[Floor] ON 
GO
INSERT [dbo].[Floor] ([FloorID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (1, 1, 1, CAST(N'2020-07-21T13:23:05.667' AS DateTime), N'sman')
GO
INSERT [dbo].[Floor] ([FloorID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, 2, 1, CAST(N'2020-07-21T13:23:05.790' AS DateTime), N'sman')
GO
INSERT [dbo].[Floor] ([FloorID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (3, 3, 1, CAST(N'2020-07-21T13:23:05.813' AS DateTime), N'sman')
GO
INSERT [dbo].[Floor] ([FloorID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (4, 4, 1, CAST(N'2020-07-21T13:23:05.820' AS DateTime), N'sman')
GO
INSERT [dbo].[Floor] ([FloorID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (5, 5, 1, CAST(N'2020-07-21T13:23:05.830' AS DateTime), N'sman')
GO
INSERT [dbo].[Floor] ([FloorID], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (6, 6, 1, CAST(N'2020-07-21T13:23:05.837' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Floor] OFF
GO
SET IDENTITY_INSERT [dbo].[Item] ON 
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (8, N'Mirchi', N'delux kaya', N'Mi001     ', 1, CAST(N'2020-07-22T07:57:41.070' AS DateTime), N'sman')
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (9, N'Sanagalu', N'vast', N'Sa002     ', 1, CAST(N'2020-07-22T07:57:41.107' AS DateTime), N'sman')
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (10, N'Kandulu', N'i dont know', N'KA103     ', 1, CAST(N'2020-07-22T07:57:41.123' AS DateTime), N'sman')
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (11, N'Pasapu', N'anty biotic', N'Pa004     ', 1, CAST(N'2020-07-22T07:57:41.137' AS DateTime), N'sman')
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (12, N'Chintapandu', N'citrus Type', N'Ch005     ', 1, CAST(N'2020-07-22T07:57:41.143' AS DateTime), N'sman')
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (13, N'Mokkajonna', N'karn', N'Mo006     ', 1, CAST(N'2020-07-22T07:57:41.153' AS DateTime), N'sman')
GO
INSERT [dbo].[Item] ([ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (14, N'Bellam', N'sugar cain product', N'Bl007     ', 1, CAST(N'2020-07-22T07:57:41.160' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Item] OFF
GO
SET IDENTITY_INSERT [dbo].[Kana] ON 
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (1, 1, 100, 1, CAST(N'2020-07-21T14:34:10.817' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, 1, 101, 1, CAST(N'2020-07-21T14:34:10.853' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (3, 1, 102, 1, CAST(N'2020-07-21T14:34:10.860' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (4, 1, 103, 1, CAST(N'2020-07-21T14:34:10.870' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (5, 1, 104, 1, CAST(N'2020-07-21T14:34:10.877' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (6, 1, 105, 1, CAST(N'2020-07-21T14:34:10.883' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (7, 1, 106, 1, CAST(N'2020-07-21T14:34:10.890' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (8, 1, 107, 1, CAST(N'2020-07-21T14:34:10.900' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (9, 1, 108, 1, CAST(N'2020-07-21T14:34:10.903' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (10, 1, 109, 1, CAST(N'2020-07-21T14:34:10.913' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (11, 1, 110, 1, CAST(N'2020-07-21T14:34:10.920' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (12, 1, 111, 1, CAST(N'2020-07-21T14:34:10.927' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (13, 1, 112, 1, CAST(N'2020-07-21T14:34:10.933' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (14, 1, 113, 1, CAST(N'2020-07-21T14:34:10.940' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (15, 1, 114, 1, CAST(N'2020-07-21T14:34:10.947' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (16, 1, 115, 1, CAST(N'2020-07-21T14:34:10.957' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (17, 1, 116, 1, CAST(N'2020-07-21T14:34:10.963' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (18, 1, 117, 1, CAST(N'2020-07-21T14:34:10.970' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (19, 1, 118, 1, CAST(N'2020-07-21T14:34:10.977' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (20, 1, 119, 1, CAST(N'2020-07-21T14:34:10.987' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (21, 1, 120, 1, CAST(N'2020-07-21T14:34:10.993' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (22, 1, 121, 1, CAST(N'2020-07-21T14:34:11.010' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (23, 1, 122, 1, CAST(N'2020-07-21T14:34:11.020' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (24, 1, 123, 1, CAST(N'2020-07-21T14:34:11.027' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (25, 1, 124, 1, CAST(N'2020-07-21T14:34:11.043' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (26, 1, 125, 1, CAST(N'2020-07-21T14:34:11.053' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (27, 1, 126, 1, CAST(N'2020-07-21T14:34:11.067' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (28, 1, 127, 1, CAST(N'2020-07-21T14:34:11.073' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (29, 1, 128, 1, CAST(N'2020-07-21T14:34:11.083' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (30, 1, 129, 1, CAST(N'2020-07-21T14:34:11.093' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (31, 1, 130, 1, CAST(N'2020-07-21T14:34:11.100' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (32, 1, 131, 1, CAST(N'2020-07-21T14:34:11.110' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (33, 1, 132, 1, CAST(N'2020-07-21T14:34:11.120' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (34, 1, 133, 1, CAST(N'2020-07-21T14:34:11.127' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (35, 1, 134, 1, CAST(N'2020-07-21T14:34:11.133' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (36, 1, 135, 1, CAST(N'2020-07-21T14:34:11.140' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (37, 1, 136, 1, CAST(N'2020-07-21T14:34:11.150' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (38, 1, 137, 1, CAST(N'2020-07-21T14:34:11.157' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (39, 1, 138, 1, CAST(N'2020-07-21T14:34:11.167' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (40, 1, 139, 1, CAST(N'2020-07-21T14:34:11.187' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (41, 1, 140, 1, CAST(N'2020-07-21T14:34:11.193' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (42, 1, 141, 1, CAST(N'2020-07-21T14:34:11.210' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (43, 1, 142, 1, CAST(N'2020-07-21T14:34:11.217' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (44, 1, 143, 1, CAST(N'2020-07-21T14:34:11.227' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (45, 1, 144, 1, CAST(N'2020-07-21T14:34:11.233' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (46, 1, 145, 1, CAST(N'2020-07-21T14:34:11.240' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (47, 1, 146, 1, CAST(N'2020-07-21T14:34:11.250' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (48, 1, 147, 1, CAST(N'2020-07-21T14:34:11.257' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (49, 1, 148, 1, CAST(N'2020-07-21T14:34:11.263' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (50, 1, 149, 1, CAST(N'2020-07-21T14:34:11.273' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (51, 1, 150, 1, CAST(N'2020-07-21T14:34:11.280' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (52, 3, 300, 1, CAST(N'2020-07-21T14:35:13.947' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (53, 3, 301, 1, CAST(N'2020-07-21T14:35:13.957' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (54, 3, 302, 1, CAST(N'2020-07-21T14:35:13.963' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (55, 3, 303, 1, CAST(N'2020-07-21T14:35:13.970' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (56, 3, 304, 1, CAST(N'2020-07-21T14:35:13.977' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (57, 3, 305, 1, CAST(N'2020-07-21T14:35:13.987' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (58, 3, 306, 1, CAST(N'2020-07-21T14:35:13.993' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (59, 3, 307, 1, CAST(N'2020-07-21T14:35:14.000' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (60, 3, 308, 1, CAST(N'2020-07-21T14:35:14.010' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (61, 3, 309, 1, CAST(N'2020-07-21T14:35:14.020' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (62, 3, 310, 1, CAST(N'2020-07-21T14:35:14.027' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (63, 3, 311, 1, CAST(N'2020-07-21T14:35:14.033' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (64, 3, 312, 1, CAST(N'2020-07-21T14:35:14.040' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (65, 3, 313, 1, CAST(N'2020-07-21T14:35:14.050' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (66, 3, 314, 1, CAST(N'2020-07-21T14:35:14.057' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (67, 3, 315, 1, CAST(N'2020-07-21T14:35:14.063' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (68, 3, 316, 1, CAST(N'2020-07-21T14:35:14.077' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (69, 3, 317, 1, CAST(N'2020-07-21T14:35:14.083' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (70, 3, 318, 1, CAST(N'2020-07-21T14:35:14.090' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (71, 3, 319, 1, CAST(N'2020-07-21T14:35:14.100' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (72, 3, 320, 1, CAST(N'2020-07-21T14:35:14.120' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (73, 3, 321, 1, CAST(N'2020-07-21T14:35:14.130' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (74, 3, 322, 1, CAST(N'2020-07-21T14:35:14.137' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (75, 3, 323, 1, CAST(N'2020-07-21T14:35:14.147' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (76, 3, 324, 1, CAST(N'2020-07-21T14:35:14.153' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (77, 3, 325, 1, CAST(N'2020-07-21T14:35:14.160' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (78, 3, 326, 1, CAST(N'2020-07-21T14:35:14.170' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (79, 3, 327, 1, CAST(N'2020-07-21T14:35:14.180' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (80, 3, 328, 1, CAST(N'2020-07-21T14:35:14.197' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (81, 3, 329, 1, CAST(N'2020-07-21T14:35:14.207' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (82, 3, 330, 1, CAST(N'2020-07-21T14:35:14.213' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (83, 3, 331, 1, CAST(N'2020-07-21T14:35:14.220' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (84, 3, 332, 1, CAST(N'2020-07-21T14:35:14.227' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (85, 3, 333, 1, CAST(N'2020-07-21T14:35:14.240' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (86, 3, 334, 1, CAST(N'2020-07-21T14:35:14.243' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (87, 3, 335, 1, CAST(N'2020-07-21T14:35:14.250' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (88, 3, 336, 1, CAST(N'2020-07-21T14:35:14.260' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (89, 3, 337, 1, CAST(N'2020-07-21T14:35:14.273' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (90, 3, 338, 1, CAST(N'2020-07-21T14:35:14.280' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (91, 3, 339, 1, CAST(N'2020-07-21T14:35:14.290' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (92, 3, 340, 1, CAST(N'2020-07-21T14:35:14.317' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (93, 3, 341, 1, CAST(N'2020-07-21T14:35:14.323' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (94, 3, 342, 1, CAST(N'2020-07-21T14:35:14.330' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (95, 3, 343, 1, CAST(N'2020-07-21T14:35:14.340' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (96, 3, 344, 1, CAST(N'2020-07-21T14:35:14.347' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (97, 3, 345, 1, CAST(N'2020-07-21T14:35:14.353' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (98, 3, 346, 1, CAST(N'2020-07-21T14:35:14.360' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (99, 3, 347, 1, CAST(N'2020-07-21T14:35:14.367' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (100, 3, 348, 1, CAST(N'2020-07-21T14:35:14.373' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (101, 3, 349, 1, CAST(N'2020-07-21T14:35:14.383' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (102, 3, 350, 1, CAST(N'2020-07-21T14:35:14.390' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (103, 4, 400, 1, CAST(N'2020-07-21T14:35:14.403' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (104, 4, 401, 1, CAST(N'2020-07-21T14:35:14.410' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (105, 4, 402, 1, CAST(N'2020-07-21T14:35:14.420' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (106, 4, 403, 1, CAST(N'2020-07-21T14:35:14.427' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (107, 4, 404, 1, CAST(N'2020-07-21T14:35:14.433' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (108, 4, 405, 1, CAST(N'2020-07-21T14:35:14.440' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (109, 4, 406, 1, CAST(N'2020-07-21T14:35:14.460' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (110, 4, 407, 1, CAST(N'2020-07-21T14:35:14.463' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (111, 4, 408, 1, CAST(N'2020-07-21T14:35:14.480' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (112, 4, 409, 1, CAST(N'2020-07-21T14:35:14.497' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (113, 4, 410, 1, CAST(N'2020-07-21T14:35:14.503' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (114, 4, 411, 1, CAST(N'2020-07-21T14:35:14.510' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (115, 4, 412, 1, CAST(N'2020-07-21T14:35:14.517' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (116, 4, 413, 1, CAST(N'2020-07-21T14:35:14.523' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (117, 4, 414, 1, CAST(N'2020-07-21T14:35:14.530' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (118, 4, 415, 1, CAST(N'2020-07-21T14:35:14.537' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (119, 4, 416, 1, CAST(N'2020-07-21T14:35:14.543' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (120, 4, 417, 1, CAST(N'2020-07-21T14:35:14.553' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (121, 4, 418, 1, CAST(N'2020-07-21T14:35:14.563' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (122, 4, 419, 1, CAST(N'2020-07-21T14:35:14.570' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (123, 4, 420, 1, CAST(N'2020-07-21T14:35:14.577' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (124, 4, 421, 1, CAST(N'2020-07-21T14:35:14.583' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (125, 4, 422, 1, CAST(N'2020-07-21T14:35:14.590' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (126, 4, 423, 1, CAST(N'2020-07-21T14:35:14.597' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (127, 4, 424, 1, CAST(N'2020-07-21T14:35:14.610' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (128, 4, 425, 1, CAST(N'2020-07-21T14:35:14.617' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (129, 4, 426, 1, CAST(N'2020-07-21T14:35:14.627' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (130, 4, 427, 1, CAST(N'2020-07-21T14:35:14.637' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (131, 4, 428, 1, CAST(N'2020-07-21T14:35:14.643' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (132, 4, 429, 1, CAST(N'2020-07-21T14:35:14.650' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (133, 4, 430, 1, CAST(N'2020-07-21T14:35:14.657' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (134, 4, 431, 1, CAST(N'2020-07-21T14:35:14.693' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (135, 4, 432, 1, CAST(N'2020-07-21T14:35:14.700' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (136, 4, 433, 1, CAST(N'2020-07-21T14:35:14.713' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (137, 4, 434, 1, CAST(N'2020-07-21T14:35:14.720' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (138, 4, 435, 1, CAST(N'2020-07-21T14:35:14.733' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (139, 4, 436, 1, CAST(N'2020-07-21T14:35:14.740' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (140, 4, 437, 1, CAST(N'2020-07-21T14:35:14.750' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (141, 4, 438, 1, CAST(N'2020-07-21T14:35:14.757' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (142, 4, 439, 1, CAST(N'2020-07-21T14:35:14.763' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (143, 4, 440, 1, CAST(N'2020-07-21T14:35:14.777' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (144, 4, 441, 1, CAST(N'2020-07-21T14:35:14.783' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (145, 4, 442, 1, CAST(N'2020-07-21T14:35:14.790' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (146, 4, 443, 1, CAST(N'2020-07-21T14:35:14.797' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (147, 4, 444, 1, CAST(N'2020-07-21T14:35:14.807' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (148, 4, 445, 1, CAST(N'2020-07-21T14:35:14.837' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (149, 4, 446, 1, CAST(N'2020-07-21T14:35:14.850' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (150, 4, 447, 1, CAST(N'2020-07-21T14:35:14.860' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (151, 4, 448, 1, CAST(N'2020-07-21T14:35:14.873' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (152, 4, 449, 1, CAST(N'2020-07-21T14:35:14.880' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (153, 4, 450, 1, CAST(N'2020-07-21T14:35:14.887' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (154, 5, 500, 1, CAST(N'2020-07-21T14:35:14.893' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (155, 5, 501, 1, CAST(N'2020-07-21T14:35:14.907' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (156, 5, 502, 1, CAST(N'2020-07-21T14:35:14.913' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (157, 5, 503, 1, CAST(N'2020-07-21T14:35:14.920' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (158, 5, 504, 1, CAST(N'2020-07-21T14:35:14.927' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (159, 5, 505, 1, CAST(N'2020-07-21T14:35:14.930' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (160, 5, 506, 1, CAST(N'2020-07-21T14:35:14.940' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (161, 5, 507, 1, CAST(N'2020-07-21T14:35:14.947' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (162, 5, 508, 1, CAST(N'2020-07-21T14:35:14.957' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (163, 5, 509, 1, CAST(N'2020-07-21T14:35:14.967' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (164, 5, 510, 1, CAST(N'2020-07-21T14:35:14.973' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (165, 5, 511, 1, CAST(N'2020-07-21T14:35:14.980' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (166, 5, 512, 1, CAST(N'2020-07-21T14:35:14.990' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (167, 5, 513, 1, CAST(N'2020-07-21T14:35:14.997' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (168, 5, 514, 1, CAST(N'2020-07-21T14:35:15.003' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (169, 5, 515, 1, CAST(N'2020-07-21T14:35:15.013' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (170, 5, 516, 1, CAST(N'2020-07-21T14:35:15.020' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (171, 5, 517, 1, CAST(N'2020-07-21T14:35:15.030' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (172, 5, 518, 1, CAST(N'2020-07-21T14:35:15.040' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (173, 5, 519, 1, CAST(N'2020-07-21T14:35:15.047' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (174, 5, 520, 1, CAST(N'2020-07-21T14:35:15.053' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (175, 5, 521, 1, CAST(N'2020-07-21T14:35:15.067' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (176, 5, 522, 1, CAST(N'2020-07-21T14:35:15.073' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (177, 5, 523, 1, CAST(N'2020-07-21T14:35:15.080' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (178, 5, 524, 1, CAST(N'2020-07-21T14:35:15.090' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (179, 5, 525, 1, CAST(N'2020-07-21T14:35:15.097' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (180, 5, 526, 1, CAST(N'2020-07-21T14:35:15.103' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (181, 5, 527, 1, CAST(N'2020-07-21T14:35:15.110' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (182, 5, 528, 1, CAST(N'2020-07-21T14:35:15.140' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (183, 5, 529, 1, CAST(N'2020-07-21T14:35:15.150' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (184, 5, 530, 1, CAST(N'2020-07-21T14:35:15.157' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (185, 5, 531, 1, CAST(N'2020-07-21T14:35:15.170' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (186, 5, 532, 1, CAST(N'2020-07-21T14:35:15.177' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (187, 5, 533, 1, CAST(N'2020-07-21T14:35:15.187' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (188, 5, 534, 1, CAST(N'2020-07-21T14:35:15.193' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (189, 5, 535, 1, CAST(N'2020-07-21T14:35:15.200' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (190, 5, 536, 1, CAST(N'2020-07-21T14:35:15.207' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (191, 5, 537, 1, CAST(N'2020-07-21T14:35:15.217' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (192, 5, 538, 1, CAST(N'2020-07-21T14:35:15.230' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (193, 5, 539, 1, CAST(N'2020-07-21T14:35:15.243' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (194, 5, 540, 1, CAST(N'2020-07-21T14:35:15.250' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (195, 5, 541, 1, CAST(N'2020-07-21T14:35:15.260' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (196, 5, 542, 1, CAST(N'2020-07-21T14:35:15.267' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (197, 5, 543, 1, CAST(N'2020-07-21T14:35:15.273' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (198, 5, 544, 1, CAST(N'2020-07-21T14:35:15.280' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (199, 5, 545, 1, CAST(N'2020-07-21T14:35:15.287' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (200, 5, 546, 1, CAST(N'2020-07-21T14:35:15.293' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (201, 5, 547, 1, CAST(N'2020-07-21T14:35:15.310' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (202, 5, 548, 1, CAST(N'2020-07-21T14:35:15.317' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (203, 5, 549, 1, CAST(N'2020-07-21T14:35:15.327' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (204, 5, 550, 1, CAST(N'2020-07-21T14:35:15.333' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (205, 6, 600, 1, CAST(N'2020-07-21T14:35:15.343' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (206, 6, 601, 1, CAST(N'2020-07-21T14:35:15.350' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (207, 6, 602, 1, CAST(N'2020-07-21T14:35:15.357' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (208, 6, 603, 1, CAST(N'2020-07-21T14:35:15.363' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (209, 6, 604, 1, CAST(N'2020-07-21T14:35:15.383' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (210, 6, 605, 1, CAST(N'2020-07-21T14:35:15.390' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (211, 6, 606, 1, CAST(N'2020-07-21T14:35:15.403' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (212, 6, 607, 1, CAST(N'2020-07-21T14:35:15.417' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (213, 6, 608, 1, CAST(N'2020-07-21T14:35:15.420' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (214, 6, 609, 1, CAST(N'2020-07-21T14:35:15.430' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (215, 6, 610, 1, CAST(N'2020-07-21T14:35:15.437' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (216, 6, 611, 1, CAST(N'2020-07-21T14:35:15.447' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (217, 6, 612, 1, CAST(N'2020-07-21T14:35:15.453' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (218, 6, 613, 1, CAST(N'2020-07-21T14:35:15.480' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (219, 6, 614, 1, CAST(N'2020-07-21T14:35:15.487' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (220, 6, 615, 1, CAST(N'2020-07-21T14:35:15.493' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (221, 6, 616, 1, CAST(N'2020-07-21T14:35:15.510' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (222, 6, 617, 1, CAST(N'2020-07-21T14:35:15.520' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (223, 6, 618, 1, CAST(N'2020-07-21T14:35:15.530' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (224, 6, 619, 1, CAST(N'2020-07-21T14:35:15.537' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (225, 6, 620, 1, CAST(N'2020-07-21T14:35:15.543' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (226, 6, 621, 1, CAST(N'2020-07-21T14:35:15.550' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (227, 6, 622, 1, CAST(N'2020-07-21T14:35:15.560' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (228, 6, 623, 1, CAST(N'2020-07-21T14:35:15.567' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (229, 6, 624, 1, CAST(N'2020-07-21T14:35:15.580' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (230, 6, 625, 1, CAST(N'2020-07-21T14:35:15.590' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (231, 6, 626, 1, CAST(N'2020-07-21T14:35:15.597' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (232, 6, 627, 1, CAST(N'2020-07-21T14:35:15.603' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (233, 6, 628, 1, CAST(N'2020-07-21T14:35:15.610' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (234, 6, 629, 1, CAST(N'2020-07-21T14:35:15.623' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (235, 6, 630, 1, CAST(N'2020-07-21T14:35:15.630' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (236, 6, 631, 1, CAST(N'2020-07-21T14:35:15.637' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (237, 6, 632, 1, CAST(N'2020-07-21T14:35:15.643' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (238, 6, 633, 1, CAST(N'2020-07-21T14:35:15.653' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (239, 6, 634, 1, CAST(N'2020-07-21T14:35:15.663' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (240, 6, 635, 1, CAST(N'2020-07-21T14:35:15.673' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (241, 6, 636, 1, CAST(N'2020-07-21T14:35:15.703' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (242, 6, 637, 1, CAST(N'2020-07-21T14:35:15.710' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (243, 6, 638, 1, CAST(N'2020-07-21T14:35:15.717' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (244, 6, 639, 1, CAST(N'2020-07-21T14:35:15.723' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (245, 6, 640, 1, CAST(N'2020-07-21T14:35:15.737' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (246, 6, 641, 1, CAST(N'2020-07-21T14:35:15.747' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (247, 6, 642, 1, CAST(N'2020-07-21T14:35:15.753' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (248, 6, 643, 1, CAST(N'2020-07-21T14:35:15.763' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (249, 6, 644, 1, CAST(N'2020-07-21T14:35:15.773' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (250, 6, 645, 1, CAST(N'2020-07-21T14:35:15.790' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (251, 6, 646, 1, CAST(N'2020-07-21T14:35:15.803' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (252, 6, 647, 1, CAST(N'2020-07-21T14:35:15.810' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (253, 6, 648, 1, CAST(N'2020-07-21T14:35:15.820' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (254, 6, 649, 1, CAST(N'2020-07-21T14:35:15.830' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (255, 6, 650, 1, CAST(N'2020-07-21T14:35:15.837' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (256, 2, 201, 1, CAST(N'2020-07-21T14:41:01.860' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (257, 2, 202, 1, CAST(N'2020-07-21T14:41:01.883' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (258, 2, 203, 1, CAST(N'2020-07-21T14:41:01.890' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (259, 2, 204, 1, CAST(N'2020-07-21T14:41:01.903' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (260, 2, 205, 1, CAST(N'2020-07-21T14:41:01.917' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (261, 2, 206, 1, CAST(N'2020-07-21T14:41:01.930' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (262, 2, 207, 1, CAST(N'2020-07-21T14:41:01.943' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (263, 2, 208, 1, CAST(N'2020-07-21T14:41:01.950' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (264, 2, 209, 1, CAST(N'2020-07-21T14:41:01.960' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (265, 2, 210, 1, CAST(N'2020-07-21T14:41:01.980' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (266, 2, 211, 1, CAST(N'2020-07-21T14:41:01.990' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (267, 2, 212, 1, CAST(N'2020-07-21T14:41:01.997' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (268, 2, 213, 1, CAST(N'2020-07-21T14:41:02.007' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (269, 2, 214, 1, CAST(N'2020-07-21T14:41:02.017' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (270, 2, 215, 1, CAST(N'2020-07-21T14:41:02.027' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (271, 2, 216, 1, CAST(N'2020-07-21T14:41:02.033' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (272, 2, 217, 1, CAST(N'2020-07-21T14:41:02.053' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (273, 2, 218, 1, CAST(N'2020-07-21T14:41:02.077' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (274, 2, 219, 1, CAST(N'2020-07-21T14:41:02.100' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (275, 2, 220, 1, CAST(N'2020-07-21T14:41:02.130' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (276, 2, 221, 1, CAST(N'2020-07-21T14:41:02.140' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (277, 2, 222, 1, CAST(N'2020-07-21T14:41:02.150' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (278, 2, 223, 1, CAST(N'2020-07-21T14:41:02.163' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (279, 2, 224, 1, CAST(N'2020-07-21T14:41:02.177' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (280, 2, 225, 1, CAST(N'2020-07-21T14:41:02.187' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (281, 2, 226, 1, CAST(N'2020-07-21T14:41:02.200' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (282, 2, 227, 1, CAST(N'2020-07-21T14:41:02.227' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (283, 2, 228, 1, CAST(N'2020-07-21T14:41:02.240' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (284, 2, 229, 1, CAST(N'2020-07-21T14:41:02.253' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (285, 2, 230, 1, CAST(N'2020-07-21T14:41:02.260' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (286, 2, 231, 1, CAST(N'2020-07-21T14:41:02.277' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (287, 2, 232, 1, CAST(N'2020-07-21T14:41:02.287' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (288, 2, 233, 1, CAST(N'2020-07-21T14:41:02.293' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (289, 2, 234, 1, CAST(N'2020-07-21T14:41:02.300' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (290, 2, 235, 1, CAST(N'2020-07-21T14:41:02.310' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (291, 2, 236, 1, CAST(N'2020-07-21T14:41:02.320' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (292, 2, 237, 1, CAST(N'2020-07-21T14:41:02.330' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (293, 2, 238, 1, CAST(N'2020-07-21T14:41:02.343' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (294, 2, 239, 1, CAST(N'2020-07-21T14:41:02.350' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (295, 2, 240, 1, CAST(N'2020-07-21T14:41:02.377' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (296, 2, 241, 1, CAST(N'2020-07-21T14:41:02.390' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (297, 2, 242, 1, CAST(N'2020-07-21T14:41:02.400' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (298, 2, 243, 1, CAST(N'2020-07-21T14:41:02.413' AS DateTime), N'sman')
GO
INSERT [dbo].[Kana] ([KanaID], [FloorID], [KanaCode], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (299, 2, 244, 1, CAST(N'2020-07-21T14:41:02.420' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Kana] OFF
GO
SET IDENTITY_INSERT [dbo].[KanaBlockMap] ON 
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, 1, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (3, 2, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (4, 3, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (5, 4, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (6, 5, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (7, 6, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (8, 7, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (9, 8, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (10, 9, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (11, 10, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (12, 11, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (13, 12, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (14, 13, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (15, 14, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (16, 15, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (17, 16, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (18, 17, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (19, 18, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (20, 19, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (21, 20, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (22, 21, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (23, 22, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (24, 23, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (25, 24, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (26, 25, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (27, 26, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (28, 27, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (29, 28, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (30, 29, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (31, 30, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (32, 31, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (33, 32, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (34, 33, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (35, 34, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (36, 35, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (37, 36, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (38, 37, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (39, 38, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (40, 39, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (41, 40, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (42, 41, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (43, 42, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (44, 43, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (45, 44, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (46, 45, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (47, 46, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (48, 47, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (49, 48, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (50, 49, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (51, 50, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (52, 51, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (53, 52, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (54, 53, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (55, 54, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (56, 55, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (57, 56, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (58, 57, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (59, 58, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (60, 59, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (61, 60, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (62, 61, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (63, 62, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (64, 63, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (65, 64, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (66, 65, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (67, 66, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (68, 67, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (69, 68, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (70, 69, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (71, 70, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (72, 71, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (73, 72, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (74, 73, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (75, 74, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (76, 75, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (77, 76, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (78, 77, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (79, 78, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (80, 79, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (81, 80, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (82, 81, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (83, 82, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (84, 83, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (85, 84, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (86, 85, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (87, 86, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (88, 87, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (89, 88, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (90, 89, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (91, 90, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (92, 91, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (93, 92, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (94, 93, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (95, 94, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (96, 95, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (97, 96, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (98, 97, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (99, 98, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (100, 99, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (101, 100, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (102, 101, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (103, 102, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (104, 103, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (105, 104, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (106, 105, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (107, 106, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (108, 107, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (109, 108, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (110, 109, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (111, 110, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (112, 111, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (113, 112, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (114, 113, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (115, 114, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (116, 115, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (117, 116, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (118, 117, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (119, 118, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (120, 119, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (121, 120, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (122, 121, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (123, 122, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (124, 123, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (125, 124, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (126, 125, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (127, 126, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (128, 127, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (129, 128, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (130, 129, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (131, 130, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (132, 131, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (133, 132, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (134, 133, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (135, 134, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (136, 135, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (137, 136, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (138, 137, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (139, 138, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (140, 139, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (141, 140, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (142, 141, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (143, 142, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (144, 143, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (145, 144, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (146, 145, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (147, 146, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (148, 147, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (149, 148, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (150, 149, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (151, 150, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (152, 151, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (153, 152, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (154, 153, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (155, 154, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (156, 155, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (157, 156, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (158, 157, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (159, 158, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (160, 159, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (161, 160, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (162, 161, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (163, 162, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (164, 163, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (165, 164, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (166, 165, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (167, 166, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (168, 167, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (169, 168, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (170, 169, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (171, 170, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (172, 171, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (173, 172, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (174, 173, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (175, 174, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (176, 175, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (177, 176, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (178, 177, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (179, 178, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (180, 179, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (181, 180, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (182, 181, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (183, 182, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (184, 183, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (185, 184, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (186, 185, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (187, 186, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (188, 187, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (189, 188, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (190, 189, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (191, 190, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (192, 191, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (193, 192, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (194, 193, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (195, 194, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (196, 195, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (197, 196, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (198, 197, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (199, 198, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (200, 199, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (201, 200, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (202, 201, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (203, 202, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (204, 203, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (205, 204, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (206, 205, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (207, 206, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (208, 207, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (209, 208, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (210, 209, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (211, 210, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (212, 211, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (213, 212, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (214, 213, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (215, 214, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (216, 215, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (217, 216, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (218, 217, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (219, 218, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (220, 219, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (221, 220, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (222, 221, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (223, 222, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (224, 223, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (225, 224, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (226, 225, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (227, 226, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (228, 227, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (229, 228, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (230, 229, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (231, 230, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (232, 231, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (233, 232, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (234, 233, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (235, 234, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (236, 235, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (237, 236, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (238, 237, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (239, 238, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (240, 239, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (241, 240, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (242, 241, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (243, 242, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (244, 243, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (245, 244, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (246, 245, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (247, 246, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (248, 247, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (249, 248, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (250, 249, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (251, 250, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (252, 251, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (253, 252, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (254, 253, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (255, 254, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (256, 255, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (257, 256, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (258, 257, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (259, 258, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (260, 259, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (261, 260, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (262, 261, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (263, 262, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (264, 263, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (265, 264, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (266, 265, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (267, 266, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (268, 267, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (269, 268, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (270, 269, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (271, 270, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (272, 271, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (273, 272, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (274, 273, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (275, 274, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (276, 275, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (277, 276, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (278, 277, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (279, 278, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (280, 279, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (281, 280, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (282, 281, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (283, 282, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (284, 283, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (285, 284, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (286, 285, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (287, 286, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (288, 287, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (289, 288, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (290, 289, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (291, 290, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (292, 291, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (293, 292, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (294, 293, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (295, 294, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (296, 295, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (297, 296, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (298, 297, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (299, 298, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (300, 299, 1, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (301, 1, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (302, 2, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (303, 3, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (304, 4, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (305, 5, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (306, 6, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (307, 7, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (308, 8, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (309, 9, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (310, 10, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (311, 11, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (312, 12, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (313, 13, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (314, 14, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (315, 15, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (316, 16, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (317, 17, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (318, 18, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (319, 19, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (320, 20, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (321, 21, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (322, 22, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (323, 23, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (324, 24, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (325, 25, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (326, 26, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (327, 27, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (328, 28, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (329, 29, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (330, 30, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (331, 31, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (332, 32, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (333, 33, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (334, 34, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (335, 35, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (336, 36, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (337, 37, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (338, 38, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (339, 39, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (340, 40, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (341, 41, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (342, 42, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (343, 43, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (344, 44, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (345, 45, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (346, 46, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (347, 47, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (348, 48, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (349, 49, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (350, 50, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (351, 51, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (352, 52, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (353, 53, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (354, 54, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (355, 55, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (356, 56, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (357, 57, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (358, 58, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (359, 59, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (360, 60, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (361, 61, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (362, 62, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (363, 63, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (364, 64, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (365, 65, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (366, 66, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (367, 67, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (368, 68, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (369, 69, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (370, 70, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (371, 71, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (372, 72, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (373, 73, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (374, 74, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (375, 75, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (376, 76, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (377, 77, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (378, 78, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (379, 79, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (380, 80, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (381, 81, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (382, 82, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (383, 83, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (384, 84, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (385, 85, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (386, 86, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (387, 87, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (388, 88, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (389, 89, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (390, 90, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (391, 91, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (392, 92, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (393, 93, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (394, 94, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (395, 95, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (396, 96, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (397, 97, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (398, 98, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (399, 99, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (400, 100, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (401, 101, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (402, 102, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (403, 103, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (404, 104, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (405, 105, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (406, 106, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (407, 107, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (408, 108, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (409, 109, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (410, 110, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (411, 111, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (412, 112, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (413, 113, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (414, 114, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (415, 115, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (416, 116, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (417, 117, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (418, 118, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (419, 119, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (420, 120, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (421, 121, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (422, 122, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (423, 123, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (424, 124, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (425, 125, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (426, 126, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (427, 127, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (428, 128, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (429, 129, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (430, 130, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (431, 131, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (432, 132, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (433, 133, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (434, 134, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (435, 135, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (436, 136, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (437, 137, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (438, 138, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (439, 139, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (440, 140, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (441, 141, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (442, 142, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (443, 143, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (444, 144, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (445, 145, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (446, 146, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (447, 147, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (448, 148, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (449, 149, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (450, 150, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (451, 151, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (452, 152, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (453, 153, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (454, 154, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (455, 155, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (456, 156, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (457, 157, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (458, 158, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (459, 159, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (460, 160, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (461, 161, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (462, 162, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (463, 163, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (464, 164, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (465, 165, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (466, 166, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (467, 167, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (468, 168, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (469, 169, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (470, 170, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (471, 171, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (472, 172, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (473, 173, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (474, 174, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (475, 175, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (476, 176, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (477, 177, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (478, 178, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (479, 179, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (480, 180, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (481, 181, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (482, 182, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (483, 183, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (484, 184, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (485, 185, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (486, 186, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (487, 187, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (488, 188, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (489, 189, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (490, 190, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (491, 191, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (492, 192, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (493, 193, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (494, 194, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (495, 195, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (496, 196, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (497, 197, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (498, 198, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (499, 199, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (500, 200, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (501, 201, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (502, 202, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (503, 203, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (504, 204, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (505, 205, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (506, 206, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (507, 207, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (508, 208, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (509, 209, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (510, 210, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (511, 211, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (512, 212, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (513, 213, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (514, 214, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (515, 215, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (516, 216, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (517, 217, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (518, 218, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (519, 219, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (520, 220, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (521, 221, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (522, 222, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (523, 223, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (524, 224, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (525, 225, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (526, 226, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (527, 227, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (528, 228, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (529, 229, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (530, 230, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (531, 231, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (532, 232, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (533, 233, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (534, 234, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (535, 235, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (536, 236, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (537, 237, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (538, 238, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (539, 239, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (540, 240, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (541, 241, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (542, 242, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (543, 243, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (544, 244, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (545, 245, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (546, 246, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (547, 247, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (548, 248, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (549, 249, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (550, 250, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (551, 251, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (552, 252, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (553, 253, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (554, 254, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (555, 255, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (556, 256, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (557, 257, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (558, 258, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (559, 259, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (560, 260, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (561, 261, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (562, 262, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (563, 263, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (564, 264, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (565, 265, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (566, 266, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (567, 267, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (568, 268, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (569, 269, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (570, 270, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (571, 271, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (572, 272, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (573, 273, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (574, 274, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (575, 275, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (576, 276, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (577, 277, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (578, 278, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (579, 279, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (580, 280, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (581, 281, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (582, 282, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (583, 283, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (584, 284, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (585, 285, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (586, 286, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (587, 287, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (588, 288, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (589, 289, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (590, 290, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (591, 291, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (592, 292, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (593, 293, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (594, 294, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (595, 295, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (596, 296, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (597, 297, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (598, 298, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (599, 299, 2, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (600, 1, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (601, 2, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (602, 3, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (603, 4, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (604, 5, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (605, 6, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (606, 7, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (607, 8, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (608, 9, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (609, 10, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (610, 11, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (611, 12, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (612, 13, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (613, 14, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (614, 15, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (615, 16, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (616, 17, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (617, 18, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (618, 19, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (619, 20, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (620, 21, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (621, 22, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (622, 23, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (623, 24, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (624, 25, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (625, 26, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (626, 27, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (627, 28, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (628, 29, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (629, 30, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (630, 31, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (631, 32, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (632, 33, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (633, 34, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (634, 35, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (635, 36, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (636, 37, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (637, 38, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (638, 39, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (639, 40, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (640, 41, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (641, 42, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (642, 43, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (643, 44, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (644, 45, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (645, 46, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (646, 47, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (647, 48, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (648, 49, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (649, 50, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (650, 51, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (651, 52, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (652, 53, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (653, 54, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (654, 55, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (655, 56, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (656, 57, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (657, 58, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (658, 59, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (659, 60, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (660, 61, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (661, 62, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (662, 63, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (663, 64, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (664, 65, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (665, 66, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (666, 67, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (667, 68, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (668, 69, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (669, 70, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (670, 71, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (671, 72, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (672, 73, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (673, 74, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (674, 75, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (675, 76, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (676, 77, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (677, 78, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (678, 79, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (679, 80, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (680, 81, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (681, 82, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (682, 83, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (683, 84, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (684, 85, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (685, 86, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (686, 87, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (687, 88, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (688, 89, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (689, 90, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (690, 91, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (691, 92, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (692, 93, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (693, 94, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (694, 95, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (695, 96, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (696, 97, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (697, 98, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (698, 99, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (699, 100, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (700, 101, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (701, 102, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (702, 103, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (703, 104, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (704, 105, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (705, 106, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (706, 107, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (707, 108, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (708, 109, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (709, 110, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (710, 111, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (711, 112, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (712, 113, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (713, 114, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (714, 115, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (715, 116, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (716, 117, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (717, 118, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (718, 119, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (719, 120, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (720, 121, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (721, 122, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (722, 123, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (723, 124, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (724, 125, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (725, 126, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (726, 127, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (727, 128, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (728, 129, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (729, 130, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (730, 131, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (731, 132, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (732, 133, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (733, 134, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (734, 135, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (735, 136, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (736, 137, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (737, 138, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (738, 139, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (739, 140, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (740, 141, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (741, 142, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (742, 143, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (743, 144, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (744, 145, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (745, 146, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (746, 147, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (747, 148, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (748, 149, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (749, 150, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (750, 151, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (751, 152, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (752, 153, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (753, 154, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (754, 155, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (755, 156, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (756, 157, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (757, 158, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (758, 159, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (759, 160, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (760, 161, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (761, 162, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (762, 163, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (763, 164, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (764, 165, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (765, 166, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (766, 167, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (767, 168, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (768, 169, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (769, 170, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (770, 171, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (771, 172, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (772, 173, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (773, 174, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (774, 175, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (775, 176, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (776, 177, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (777, 178, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (778, 179, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (779, 180, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (780, 181, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (781, 182, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (782, 183, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (783, 184, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (784, 185, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (785, 186, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (786, 187, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (787, 188, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (788, 189, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (789, 190, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (790, 191, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (791, 192, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (792, 193, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (793, 194, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (794, 195, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (795, 196, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (796, 197, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (797, 198, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (798, 199, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (799, 200, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (800, 201, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (801, 202, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (802, 203, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (803, 204, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (804, 205, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (805, 206, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (806, 207, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (807, 208, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (808, 209, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (809, 210, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (810, 211, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (811, 212, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (812, 213, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (813, 214, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (814, 215, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (815, 216, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (816, 217, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (817, 218, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (818, 219, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (819, 220, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (820, 221, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (821, 222, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (822, 223, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (823, 224, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (824, 225, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (825, 226, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (826, 227, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (827, 228, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (828, 229, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (829, 230, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (830, 231, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (831, 232, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (832, 233, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (833, 234, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (834, 235, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (835, 236, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (836, 237, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (837, 238, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (838, 239, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (839, 240, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (840, 241, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (841, 242, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (842, 243, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (843, 244, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (844, 245, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (845, 246, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (846, 247, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (847, 248, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (848, 249, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (849, 250, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (850, 251, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (851, 252, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (852, 253, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (853, 254, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (854, 255, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (855, 256, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (856, 257, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (857, 258, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (858, 259, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (859, 260, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (860, 261, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (861, 262, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (862, 263, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (863, 264, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (864, 265, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (865, 266, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (866, 267, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (867, 268, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (868, 269, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (869, 270, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (870, 271, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (871, 272, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (872, 273, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (873, 274, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (874, 275, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (875, 276, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (876, 277, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (877, 278, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (878, 279, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (879, 280, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (880, 281, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (881, 282, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (882, 283, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (883, 284, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (884, 285, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (885, 286, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (886, 287, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (887, 288, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (888, 289, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (889, 290, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (890, 291, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (891, 292, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (892, 293, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (893, 294, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (894, 295, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (895, 296, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (896, 297, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (897, 298, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
INSERT [dbo].[KanaBlockMap] ([KanaBlockMapID], [KanaID], [BlockID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (898, 299, 3, 1, CAST(N'2020-07-21T16:49:50.290' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[KanaBlockMap] OFF
GO
SET IDENTITY_INSERT [dbo].[Loan] ON 
GO
INSERT [dbo].[Loan] ([LoanID], [TransactionID], [FarmerID], [BankID], [BondNumber], [NetWeight], [ApprxCost], [AmountEligible], [AmountSanctioned], [RequestDate], [ApproveDate], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (10, 7, 2, 1, 558, 1890, 225000, 90000, 80000, CAST(N'2020-07-25T16:22:46.093' AS DateTime), CAST(N'2020-07-25T16:22:46.093' AS DateTime), 1, CAST(N'2020-07-25T17:28:15.153' AS DateTime), N'sman')
GO
INSERT [dbo].[Loan] ([LoanID], [TransactionID], [FarmerID], [BankID], [BondNumber], [NetWeight], [ApprxCost], [AmountEligible], [AmountSanctioned], [RequestDate], [ApproveDate], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (11, 8, 3, 1, 559, 3528, 490000, 168000, 80000, CAST(N'2020-07-25T16:22:46.093' AS DateTime), CAST(N'2020-07-25T16:22:46.093' AS DateTime), 1, CAST(N'2020-07-26T15:28:01.427' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Loan] OFF
GO
SET IDENTITY_INSERT [dbo].[RecordStatus] ON 
GO
INSERT [dbo].[RecordStatus] ([RecordStatusID], [Code], [Name], [CreatedDate], [CreatedUser]) VALUES (1, N'A         ', N'Active    ', CAST(N'2020-07-21T11:48:53.920' AS DateTime), N'sman')
GO
INSERT [dbo].[RecordStatus] ([RecordStatusID], [Code], [Name], [CreatedDate], [CreatedUser]) VALUES (2, N'I         ', N'InActive  ', CAST(N'2020-07-21T11:48:53.963' AS DateTime), N'sman')
GO
INSERT [dbo].[RecordStatus] ([RecordStatusID], [Code], [Name], [CreatedDate], [CreatedUser]) VALUES (3, N'D         ', N'Delete    ', CAST(N'2020-07-21T11:48:53.980' AS DateTime), N'sman')
GO
INSERT [dbo].[RecordStatus] ([RecordStatusID], [Code], [Name], [CreatedDate], [CreatedUser]) VALUES (4, N'AP        ', N'Approved  ', CAST(N'2020-07-21T11:48:53.987' AS DateTime), N'sman')
GO
INSERT [dbo].[RecordStatus] ([RecordStatusID], [Code], [Name], [CreatedDate], [CreatedUser]) VALUES (5, N'R         ', N'Rejected  ', CAST(N'2020-07-21T11:48:53.993' AS DateTime), N'sman')
GO
INSERT [dbo].[RecordStatus] ([RecordStatusID], [Code], [Name], [CreatedDate], [CreatedUser]) VALUES (6, N'S         ', N'Settled   ', CAST(N'2020-07-21T11:48:54.000' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[RecordStatus] OFF
GO
SET IDENTITY_INSERT [dbo].[Transaction] ON 
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (7, NULL, 1, 2, NULL, 8, 1, 45, 2, 1, CAST(N'2020-07-22T17:44:22.527' AS DateTime), N'sman')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (8, NULL, 2, 3, NULL, 8, 1, 84, 3, 1, CAST(N'2020-07-26T15:26:45.343' AS DateTime), N'sman')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (9, NULL, 1, 6, NULL, 8, 1, 21, 3, 1, CAST(N'2020-09-11T15:11:22.557' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (10, NULL, 2, 6, NULL, 8, 1, 4, 3, 1, CAST(N'2020-09-11T15:11:37.807' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (11, NULL, 2, 6, NULL, 8, 1, 6, 3, 1, CAST(N'2020-09-11T15:11:49.890' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (12, NULL, 1, 7, NULL, 8, 1, 88, 3, 1, CAST(N'2020-09-11T15:12:42.080' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (13, NULL, 1, 7, NULL, 8, 1, 14, 3, 1, CAST(N'2020-09-11T15:12:57.390' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (14, NULL, 1, 7, NULL, 8, 1, 5, 3, 1, CAST(N'2020-09-11T15:13:07.963' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (15, NULL, 1, 5, NULL, 8, 1, 10, 3, 1, CAST(N'2020-09-11T15:14:08.293' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
INSERT [dbo].[Transaction] ([TransactionID], [ParentTransactionID], [TransactionTypeID], [FarmerID], [Description], [ItemID], [VarietyID], [NoOfBags], [KanaBlockMapID], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (16, NULL, 2, 5, NULL, 8, 1, 9, 3, 1, CAST(N'2020-09-11T15:14:36.280' AS DateTime), N'DESKTOP-N14N647\sambasivarao')
GO
SET IDENTITY_INSERT [dbo].[Transaction] OFF
GO
SET IDENTITY_INSERT [dbo].[TransactionType] ON 
GO
INSERT [dbo].[TransactionType] ([TransactionTypeID], [Name], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (1, N'checkin', 1, CAST(N'2020-07-21T12:35:46.837' AS DateTime), N'sman')
GO
INSERT [dbo].[TransactionType] ([TransactionTypeID], [Name], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, N'checkout', 1, CAST(N'2020-07-21T12:35:46.873' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[TransactionType] OFF
GO
SET IDENTITY_INSERT [dbo].[Variety] ON 
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (1, 8, N'Nallurisannalu', N'', N'NS001     ', 1, CAST(N'2020-07-22T08:37:21.663' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (2, 8, N'talu kayalu', N'', N'TLU000    ', 1, CAST(N'2020-07-22T08:37:21.677' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (3, 8, N'delux', N'', N'DLX       ', 1, CAST(N'2020-07-22T08:37:21.697' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (4, 13, N'popcorn', N'', N'PoP001    ', 1, CAST(N'2020-07-22T08:37:21.707' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (5, 14, N'Black', N'', N'Bk001     ', 1, CAST(N'2020-07-22T08:37:21.713' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (6, 8, N'Teja', N'fire', N'TJ001     ', 1, CAST(N'2020-07-22T08:37:34.913' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (7, 8, N'22', N'', N'22002     ', 1, CAST(N'2020-07-22T08:37:34.930' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (8, 9, N'Black', N'', N'SA003     ', 1, CAST(N'2020-07-22T08:37:34.940' AS DateTime), N'sman')
GO
INSERT [dbo].[Variety] ([VarietyID], [ItemID], [Name], [Description], [Code], [RecordStatusID], [CreatedDate], [CreatedUser]) VALUES (9, 9, N'White', N'', N'SA004     ', 1, CAST(N'2020-07-22T08:37:34.947' AS DateTime), N'sman')
GO
SET IDENTITY_INSERT [dbo].[Variety] OFF
GO
/****** Object:  Index [I_DONT_CARE_U_ALREDY_EXIST]    Script Date: 18/12/2020 9:04:30 am ******/
ALTER TABLE [dbo].[Farmer] ADD  CONSTRAINT [I_DONT_CARE_U_ALREDY_EXIST] UNIQUE NONCLUSTERED 
(
	[Phone] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_Floor]    Script Date: 18/12/2020 9:04:30 am ******/
ALTER TABLE [dbo].[Floor] ADD  CONSTRAINT [IX_Floor] UNIQUE NONCLUSTERED 
(
	[FloorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [IX_Kana]    Script Date: 18/12/2020 9:04:30 am ******/
ALTER TABLE [dbo].[Kana] ADD  CONSTRAINT [IX_Kana] UNIQUE NONCLUSTERED 
(
	[KanaID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [BondNumber]    Script Date: 18/12/2020 9:04:30 am ******/
ALTER TABLE [dbo].[Loan] ADD  CONSTRAINT [BondNumber] UNIQUE NONCLUSTERED 
(
	[BondNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Bank] ADD  CONSTRAINT [DF_Bank_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Bank] ADD  CONSTRAINT [DF_Bank_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Block] ADD  CONSTRAINT [DF_Block_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Block] ADD  CONSTRAINT [DF_Block_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Farmer] ADD  CONSTRAINT [DF_Farmer_EffFromDate]  DEFAULT (getdate()) FOR [EffFromDate]
GO
ALTER TABLE [dbo].[Farmer] ADD  CONSTRAINT [DF_Farmer_EffThruDate]  DEFAULT ('9999-01-01') FOR [EffThruDate]
GO
ALTER TABLE [dbo].[Farmer] ADD  CONSTRAINT [DF_Farmer_RecordStatusID]  DEFAULT ((1)) FOR [RecordStatusID]
GO
ALTER TABLE [dbo].[Farmer] ADD  CONSTRAINT [DF_Farmer_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Farmer] ADD  CONSTRAINT [DF_Farmer_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Floor] ADD  CONSTRAINT [DF_Floor_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Floor] ADD  CONSTRAINT [DF_Floor_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Item] ADD  CONSTRAINT [DF_Item_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Item] ADD  CONSTRAINT [DF_Item_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Kana] ADD  CONSTRAINT [DF_Kana_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Kana] ADD  CONSTRAINT [DF_Kana_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[KanaBlockMap] ADD  CONSTRAINT [DF_KanaBlockMap_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[KanaBlockMap] ADD  CONSTRAINT [DF_KanaBlockMap_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Loan] ADD  CONSTRAINT [DF_Loan_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Loan] ADD  CONSTRAINT [DF_Loan_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[RecordStatus] ADD  CONSTRAINT [DF_RecordStatus_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[RecordStatus] ADD  CONSTRAINT [DF_RecordStatus_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Transaction] ADD  CONSTRAINT [DF_Transaction_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Transaction] ADD  CONSTRAINT [DF_Transaction_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[TransactionType] ADD  CONSTRAINT [DF_TransactionType_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[TransactionType] ADD  CONSTRAINT [DF_TransactionType_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Variety] ADD  CONSTRAINT [DF_Variety_CreatedDate]  DEFAULT (getdate()) FOR [CreatedDate]
GO
ALTER TABLE [dbo].[Variety] ADD  CONSTRAINT [DF_Variety_CreatedUser]  DEFAULT (suser_sname()) FOR [CreatedUser]
GO
ALTER TABLE [dbo].[Bank]  WITH CHECK ADD  CONSTRAINT [FK_Bank_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Bank] CHECK CONSTRAINT [FK_Bank_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Block]  WITH CHECK ADD  CONSTRAINT [FK_Block_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Block] CHECK CONSTRAINT [FK_Block_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Farmer]  WITH CHECK ADD  CONSTRAINT [FK_Farmer_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Farmer] CHECK CONSTRAINT [FK_Farmer_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Floor]  WITH CHECK ADD  CONSTRAINT [FK_Floor_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Floor] CHECK CONSTRAINT [FK_Floor_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Item]  WITH CHECK ADD  CONSTRAINT [FK_Item_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Item] CHECK CONSTRAINT [FK_Item_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Kana]  WITH CHECK ADD  CONSTRAINT [FK_Kana_FloorID_Floor_FloorID] FOREIGN KEY([FloorID])
REFERENCES [dbo].[Floor] ([FloorID])
GO
ALTER TABLE [dbo].[Kana] CHECK CONSTRAINT [FK_Kana_FloorID_Floor_FloorID]
GO
ALTER TABLE [dbo].[Kana]  WITH CHECK ADD  CONSTRAINT [FK_Kana_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Kana] CHECK CONSTRAINT [FK_Kana_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[KanaBlockMap]  WITH CHECK ADD  CONSTRAINT [FK_KanaBlockMap_BlockID_Block_BlockID] FOREIGN KEY([BlockID])
REFERENCES [dbo].[Block] ([BlockID])
GO
ALTER TABLE [dbo].[KanaBlockMap] CHECK CONSTRAINT [FK_KanaBlockMap_BlockID_Block_BlockID]
GO
ALTER TABLE [dbo].[KanaBlockMap]  WITH CHECK ADD  CONSTRAINT [FK_KanaBlockMap_KanaID_Kana_KanaID] FOREIGN KEY([KanaID])
REFERENCES [dbo].[Kana] ([KanaID])
GO
ALTER TABLE [dbo].[KanaBlockMap] CHECK CONSTRAINT [FK_KanaBlockMap_KanaID_Kana_KanaID]
GO
ALTER TABLE [dbo].[KanaBlockMap]  WITH CHECK ADD  CONSTRAINT [FK_KanaBlockMap_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[KanaBlockMap] CHECK CONSTRAINT [FK_KanaBlockMap_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_BankID_Bank_BankID] FOREIGN KEY([BankID])
REFERENCES [dbo].[Bank] ([BankID])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_BankID_Bank_BankID]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_FarmerID_Farmer_FarmerID] FOREIGN KEY([FarmerID])
REFERENCES [dbo].[Farmer] ([FarmerID])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_FarmerID_Farmer_FarmerID]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_TransactionID_Transaction_TransactionID] FOREIGN KEY([TransactionID])
REFERENCES [dbo].[Transaction] ([TransactionID])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_TransactionID_Transaction_TransactionID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_FarmerID_Farmer_FarmerID] FOREIGN KEY([FarmerID])
REFERENCES [dbo].[Farmer] ([FarmerID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_FarmerID_Farmer_FarmerID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_ItemID_Item_ItemID] FOREIGN KEY([ItemID])
REFERENCES [dbo].[Item] ([ItemID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_ItemID_Item_ItemID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_KanaBlockMapID_KanaBlockMap_KanaBlockMapID] FOREIGN KEY([KanaBlockMapID])
REFERENCES [dbo].[KanaBlockMap] ([KanaBlockMapID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_KanaBlockMapID_KanaBlockMap_KanaBlockMapID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_ParentTransactionID_Transaction_TransactionID] FOREIGN KEY([ParentTransactionID])
REFERENCES [dbo].[Transaction] ([TransactionID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_ParentTransactionID_Transaction_TransactionID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_RecordStatusID_RecordStatus_RecordStatusID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_TransactionTypeID_TransactionType_TransactionTypeID] FOREIGN KEY([TransactionTypeID])
REFERENCES [dbo].[TransactionType] ([TransactionTypeID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_TransactionTypeID_TransactionType_TransactionTypeID]
GO
ALTER TABLE [dbo].[Transaction]  WITH CHECK ADD  CONSTRAINT [FK_Transaction_VarietyID_Variety_VarietyID] FOREIGN KEY([VarietyID])
REFERENCES [dbo].[Variety] ([VarietyID])
GO
ALTER TABLE [dbo].[Transaction] CHECK CONSTRAINT [FK_Transaction_VarietyID_Variety_VarietyID]
GO
ALTER TABLE [dbo].[Variety]  WITH CHECK ADD  CONSTRAINT [FK_Variety_ItemID_Item_ItemID] FOREIGN KEY([ItemID])
REFERENCES [dbo].[Item] ([ItemID])
GO
ALTER TABLE [dbo].[Variety] CHECK CONSTRAINT [FK_Variety_ItemID_Item_ItemID]
GO
ALTER TABLE [dbo].[Variety]  WITH CHECK ADD  CONSTRAINT [FK_Variety_RecordStatusID_RecordStatus_RecordStatusID] FOREIGN KEY([RecordStatusID])
REFERENCES [dbo].[RecordStatus] ([RecordStatusID])
GO
ALTER TABLE [dbo].[Variety] CHECK CONSTRAINT [FK_Variety_RecordStatusID_RecordStatus_RecordStatusID]
GO
/****** Object:  StoredProcedure [dbo].[BANKI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[BANKI]
@Name VARCHAR(225)
,@address VARCHAR(4000)
,@phone VARCHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Bank WHERE NAME = @Name)
	BEGIN
		INSERT INTO Bank(Name,address,phone,RecordStatusID)
		VALUES (@Name,@address,@phone,@RecordStatusID)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[BankUpdate]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[BankUpdate]
@Name VARCHAR(255) null
,@Address VARCHAR(4000) null
,@Phone Varchar(10) null
AS
BEGIN
UPDATE Bank set [Name] = isnull(@Name,[Name])
               ,[Address] = ISNULL(@Address,[Address])
			   ,[Phone] = ISNULL(@Phone,[Phone])
Where BankID = (Select BankID from Bank Where Name = @Name or Phone = @Phone)

END
GO
/****** Object:  StoredProcedure [dbo].[Bill]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create proc [dbo].[Bill]
@Phone     BIGINT
As 
begin
SELECT DISTINCT Farmer,PHONE,VILLAGE
,UPPER(FORMAT(Transactiondate,'dd-MMM-yyyy')) FROM_DATE,
UPPER(FORMAT(GETDATE(),'dd-MMM-yyyy')) TO_DATE
,(DATEDIFF(YEAR,TransactionDATE, GETDATE())/1)+1 YERAS
,FORMAT((select C.AmountSanctioned from loan where C.RecordStatusID = 1 ),'C0','HI-in') LOAN
,C.BondNumber,
FORMAT((select sum(noofbags) from v_Transaction where TransactionTypeID = 1 and TransactionStatus = 'Active' and Phone = @phone) *(((DATEDIFF(YEAR,Transactiondate, GETDATE())/1)+1)*170),'C0','HI-in') REAL_RENT FROM v_Transaction A

LEFT JOIN LOAN C ON A.FARMERID = C.FARMERID
where Phone= @Phone
End
GO
/****** Object:  StoredProcedure [dbo].[BLOCKI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[BLOCKI]
 @Code CHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM [Block] WHERE Code = @Code)
	BEGIN
		INSERT INTO [Block] (Code,RecordStatusID)
		VALUES (@Code,@RecordStatusID)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[FarmerI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[FarmerI]
 @FirstName VARCHAR(225)
,@LastName VARCHAR(225)
,@Village VARCHAR(225)
,@Mandal VARCHAR(225)
,@PANNumber CHAR(25)
,@Phone BIGINT
,@Aadhar BIGINT

AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Farmer WHERE PanNumber = @PanNumber)
	BEGIN
		INSERT INTO farmer (FirstName,LastName,Village,Mandal,PANNumber,Phone,Aadhar,RecordStatusID)
		VALUES (@FirstName,@LastName,@Village,@Mandal,@PANNumber,@Phone,@Aadhar,1)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[FarmerSearch]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[FarmerSearch]
@Phone BIGINT
AS
BEGIN
 
SELECT FirstName,LastName,Village,Mandal,PANNumber,EffFromDate,Phone,Aadhar FROM Farmer WHERE Phone = @Phone
END
GO
/****** Object:  StoredProcedure [dbo].[FarmerUpdate]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[FarmerUpdate]
 @FirstName  VARCHAR(225) null
,@LastName  VARCHAR(225) null
,@Village   VARCHAR(225) null
,@Mandal    VARCHAR(225) null
,@PANNumber CHAR(25) null
,@Phone     BIGINT	 null
,@Aadhar    BIGINT	 null
AS
BEGIN

update Farmer set FirstName = ISNULL(@FirstName ,FirstName) 
                 ,LastName = ISNULL(@LastName,LastName)
				 ,Village = ISNULL(@Village,Village)
				 ,Mandal = ISNULL(@Mandal,Mandal)
				 ,PANNumber = ISNULL(@PANNumber,PANNumber)
				 ,Phone = ISNULL(@Phone,Phone)
				 ,Aadhar = ISNULL(@Aadhar,Aadhar)
where FarmerID = (select FarmerID from Farmer where FirstName = @FirstName and LastName = @LastName or Phone = @Phone)

end
GO
/****** Object:  StoredProcedure [dbo].[FLOORI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[FLOORI]
 @Code INT
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Floor WHERE Code = @Code)
	BEGIN
		INSERT INTO Floor (Code,RecordStatusID)
		VALUES (@Code,@RecordStatusID)
	END
END
 
GO
/****** Object:  StoredProcedure [dbo].[ItemI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[ItemI]
 @Name nvarchar(100)
,@Description nvarchar(4000)
,@Code CHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Item WHERE Code = @Code)
	BEGIN
		INSERT INTO Item (Name,Description,Code,RecordStatusID)
		VALUES (@Name,@Description,@Code,@RecordStatusID)
	END
END
GO
/****** Object:  StoredProcedure [dbo].[ItemUpdate]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[ItemUpdate]
 @Name NVARCHAR(100) NULL
,@Description NVARCHAR(4000) NULL
,@Code NCHAR(10) NULL
AS
BEGIN
UPDATE Item set [Name] = ISNULL(@Name,Name)
              ,[Description] = isnull(@Description,[Description])
			  ,[Code] = ISNULL (@Code,Code)
Where ItemID = (Select ItemID From Item Where [Name] = @Name OR Code = @COde)

END
GO
/****** Object:  StoredProcedure [dbo].[KanaBlockMapI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE procedure [dbo].[KanaBlockMapI]
as
begin
	declare 
	          @recordstatusid int,
              @KanaID int,
			  @FloorID int,
			  @Kanacode int,
			  @Blockid int,
			  @Blockcode char(10)
		insert into kanablockmap (recordstatusID,kanaid,blockid)
		
	SELECT c.* FROM 
(select  1 AS recordstatusID,
a.kanaid,b.[blockid] from kana a
cross apply block b
) c left join KanaBlockMap KBM ON c.KanaID = KBM.KanaID AND c.blockID = KBM.BlockID
WHERE KBM.KanaBlockMapID IS NULL

 end
GO
/****** Object:  StoredProcedure [dbo].[KANAI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[KANAI]
 @FLOORID INT
,@STARTING_NUMBER INT
,@ENDING_NUMBER INT AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM KANA WHERE FLOORID = @FLOORID)
	begin  
      declare 
              @KANACODE INT
			  ,@RecordStatusID INT
SELECT 
@RecordStatusID  = '1'
 SET @KANACODE  =    @STARTING_NUMBER
WHILE  @KANACODE  <= @ENDING_NUMBER
BEGIN
 INSERT INTO KANA  (FLOORID,
                    KANACODE,
					RecordStatusID
					) 
			      

 VALUES (@FLOORID,
         @KANACODE,
		 @RecordStatusID
		 )
SET @KANACODE  =  @KANACODE  + 1 END;
		 END
END
GO
/****** Object:  StoredProcedure [dbo].[LoanI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[LoanI]
 @BondNumber INT
,@AvgBagWeight int
,@MarketPrise int
,@LoanForBag int
,@AmountSanctioned FLOAT
,@RequestDate DATETIME
,@ApproveDate DATETIME
,@FarmerID INT
,@BankID int
AS 
BEGIN
Declare @NetWeight int
       ,@ApprxCost FLOAT
       ,@AmountEligible Float
	   ,@TransactionID int
	   ,@RecordStatusID int
 SELECT @RecordStatusID = 1,@TransactionID = [TransactionID],@NetWeight = CONVERT(FLOAT,((NoOfBags)*@AvgBagWeight))
      ,@ApprxCost = (((NoOfBags)*@AvgBagWeight/100)*@MarketPrise)
	  ,@AmountEligible = (NoOfBags*@LoanForBag)  FROM [TRANSACTION]
	 
	  WHERE FarmerID = @FarmerID

INSERT INTO Loan (RecordStatusID,BankID,FarmerID,TransactionID,BondNumber,NetWeight,ApprxCost,AmountEligible,AmountSanctioned,RequestDate,ApproveDate)
VALUES (@RecordStatusID,@BankID,@FarmerID,@TransactionID,@BondNumber,@NetWeight,@ApprxCost,@AmountEligible,@AmountSanctioned,@RequestDate,@ApproveDate)
END
GO
/****** Object:  StoredProcedure [dbo].[LoanUpdate]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[LoanUpdate]
 @BondNumber INT null
,@AmountSanctioned FLOAT null
,@RequestDate DATETIME null
,@ApproveDate DATETIME null
,@FarmerID INT
,@TransactionID int
AS 
BEGIN
	IF  EXISTS(SELECT RecordStatusID FROM Loan WHERE FarmerID = @FarmerID and RecordStatusID = 1 and TransactionID = @TransactionID)
BEGIN
Update Loan
set BondNumber = isnull(@BondNumber,BondNumber)
   ,AmountSanctioned = isnull(@AmountSanctioned,AmountSanctioned)
   ,RequestDate = isnull(@RequestDate,RequestDate)
   ,ApproveDate = isnull(@ApproveDate,ApproveDate)
	  WHERE FarmerID = @FarmerID and TransactionID = @TransactionID
   END
END
GO
/****** Object:  StoredProcedure [dbo].[p_FarmerSearch]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[p_FarmerSearch]
@Phone BIGINT
AS
BEGIN
/*
EXEC p_FarmerSearch  @Phone = '8099892109' 
*/
SELECT FirstName,LastName,Village,Mandal,PANNumber,EffFromDate,Phone,Aadhar,R.RecordStatusID,R.Name Status FROM Farmer F
	JOIN RecordStatus R ON R.RecordStatusID = F.RecordStatusID WHERE Phone = @Phone
END
GO
/****** Object:  StoredProcedure [dbo].[p_GetCustmerByPhone]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[p_GetCustmerByPhone]
@Phone BIGINT
AS
BEGIN
/*
EXEC p_FarmerSearch  @Phone = '8099892109' 
*/
SELECT FirstName,LastName,Village,Mandal,PANNumber,EffFromDate,Phone,Aadhar,R.RecordStatusID,R.Name Status,dbo.NoOfBags_Balance (FarmerID) Balance_Bags FROM Farmer F
	JOIN RecordStatus R ON R.RecordStatusID = F.RecordStatusID WHERE Phone = @Phone
END
GO
/****** Object:  StoredProcedure [dbo].[p_GetCustmerTransactionsByDate]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create procedure [dbo].[p_GetCustmerTransactionsByDate]
 @FromDate DATETIME
,@ToDate DATETIME
as
begin
SELECT * FROM v_Transaction
where TransactionDate >= @FromDate and TransactionDate <= @ToDate
end
GO
/****** Object:  StoredProcedure [dbo].[p_GetCustmerTransactionsByPhone]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROC [dbo].[p_GetCustmerTransactionsByPhone]
@Phone BIGINT 
AS
BEGIN
	SELECT 
	 Farmer
    ,Village
    ,Phone
    ,NoOfBags
    ,TransactionID
    ,Description
    ,TransactionTypeID
    ,TransactionType
    ,ItemID
    ,Item
    ,VarietyID
    ,Variety
    ,KanaBlockKey
    ,TransactionStatus
FROM v_Transaction
	WHERE Phone = @Phone
END
GO
/****** Object:  StoredProcedure [dbo].[RecordStatusI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[RecordStatusI]
@Name NCHAR(10)
,@Code NCHAR(10)
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM RecordStatus WHERE Code = @Code)
	BEGIN
		INSERT INTO RecordStatus (Name,Code)
		VALUES (@Name,@Code)
	END
END
 
GO
/****** Object:  StoredProcedure [dbo].[TransactionI]    Script Date: 18/12/2020 9:04:30 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[TransactionI]
 @FirstName VARCHAR(225)
,@Phone BIGINT
,@NoOfBags INT
,@Description NVARCHAR(4000) = NULL
,@TransactionTypeID INT
,@ItemID INT
,@VarietyID INT
,@KanaBlockMapID INT
as
Begin
declare
 @FarmerID INT
,@RecordStatusID INT

SELECT @FarmerID = A.FarmerID
,@RecordStatusID = 1 FROM Farmer A
 join RecordStatus G on G.RecordStatusID = A.RecordStatusID
 WHERE A.FirstName  = @FirstName or A.Phone = @Phone
 INSERT INTO [Transaction] ( FarmerID
                            ,RecordStatusID
                            ,TransactionTypeID
    					    ,ItemID
						    ,VarietyID
						    ,KanaBlockMapID
						    ,NoOfBags
						    ,Description)
               
			     VALUES (    @FarmerID
				            ,@RecordStatusID
				            ,@TransactionTypeID
    					    ,@ItemID
						    ,@VarietyID
						    ,@KanaBlockMapID
						    ,@NoOfBags
						    ,@Description)
END
GO
/****** Object:  StoredProcedure [dbo].[TRANSACTIONTYPEI]    Script Date: 18/12/2020 9:04:31 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[TRANSACTIONTYPEI]
 @Name NVARCHAR(50)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM TRANSACTIONTYPE WHERE NAME = @NAME)
	BEGIN
		INSERT INTO TRANSACTIONTYPE (Name,RecordStatusID)
		VALUES (@Name,@RecordStatusID)
	END
END
 

 SELECT * FROM TRANSACTIONTYPEI

 EXEC dbo.TRANSACTIONTYPEI 'checkin', '1'
 EXEC dbo.TRANSACTIONTYPEI 'checkout', '1'
GO
/****** Object:  StoredProcedure [dbo].[TransactionUpdate]    Script Date: 18/12/2020 9:04:31 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create Procedure [dbo].[TransactionUpdate]
 @FarmerID int
,@TransactionID int null
,@Description nvarchar(4000) NULL
,@ItemID int NULL
,@VarietyID int NULL
,@NoOfBags int NULL
,@KanaBlockMapID int NULL
AS
BEGIN
	IF  EXISTS(SELECT RecordStatusID FROM [TRANSACTION] WHERE FarmerID = @FarmerID and RecordStatusID = 1 and TransactionID = @TransactionID)
	BEGIN
update [transaction] 
set NoOfBags = ISNULL(@NoOfBags,NoOfBags)
   ,KanaBlockMapID = ISNULL(@KanaBlockMapID,KanaBlockMapID)
   ,[Description] = ISNULL(@Description,[Description])
   ,ItemID = ISNULL(@ItemID,ItemID)
   ,VarietyID = ISNULL(@VarietyID,VarietyID)
where FarmerID = @FarmerID and TransactionID = @TransactionID
  END
END
GO
/****** Object:  StoredProcedure [dbo].[VarietyI]    Script Date: 18/12/2020 9:04:31 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[VarietyI]
 @ItemID int
,@Name nvarchar(100)
,@Description nvarchar(4000)
,@Code NCHAR(10)
,@RecordStatusID INT
AS
BEGIN
	IF NOT EXISTS(SELECT 1 FROM Variety WHERE Code = @Code)
	BEGIN
		INSERT INTO Variety (ItemID,Name,Description,Code,RecordStatusID)
		VALUES (@ItemID,@Name,@Description,@Code,@RecordStatusID)
	END
END
 
GO
/****** Object:  StoredProcedure [dbo].[VarietyUpdate]    Script Date: 18/12/2020 9:04:31 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[VarietyUpdate]
 @Name NVARCHAR(100) NULL
,@Description NVARCHAR(4000) NULL
,@Code NCHAR(10) NULL
AS
BEGIN
UPDATE Variety set [Name] = ISNULL(@Name,Name)
              ,[Description] = isnull(@Description,[Description])
			  ,[Code] = ISNULL (@Code,Code)
Where VarietyID = (Select VarietyID From Variety Where [Name] = @Name OR Code = @COde)

END
GO
USE [master]
GO
ALTER DATABASE [littleking] SET  READ_WRITE 
GO
