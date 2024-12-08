'use client'

import { api } from '@/lib/axios'
import { create } from 'zustand'

interface User {
  id: number
  username: string
  email: string
  first_name: string
  last_name: string
}

interface AuthState {
  user: User | null
  isLoading: boolean
  error: string | null
  getUser: () => Promise<void>
  logout: () => Promise<void>
}

export const useAuth = create<AuthState>((set) => ({
  user: null,
  isLoading: true,
  error: null,
  getUser: async () => {
    try {
      set({ isLoading: true, error: null })
      const response = await api.get('/auth/user/')
      set({ user: response.data, isLoading: false })
    } catch (error) {
      set({ user: null, isLoading: false, error: 'Failed to get user' })
    }
  },
  logout: async () => {
    try {
      await api.post('/auth/logout/')
      set({ user: null, error: null })
    } catch (error) {
      set({ error: 'Failed to logout' })
    }
  },
}))
