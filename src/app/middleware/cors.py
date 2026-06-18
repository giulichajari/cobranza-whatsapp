app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego restringes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)